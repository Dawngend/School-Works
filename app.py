import streamlit as st
import random
import json
import os
import database as db 
from generator import generate_custom_deck # Hooking up Andy's brain!

# ── Theme & Configuration ────────────────────────────────────────────────────
st.set_page_config(page_title="Andy: Your Study Buddy", layout="wide")

# Baseline Blue & Cream CSS (You can overwrite this later with your UI app)
st.markdown("""
    <style>
    .stApp {
        background-color: #FDFDF9; /* Soft Cream */
        color: #1A365D; /* Navy Blue */
    }
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        color: #1A365D !important; 
    }
    .stButton>button {
        background-color: #2B6CB0; /* Nice readable blue */
        color: #FDFDF9;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #1A365D;
        color: #FDFDF9;
    }
    .stSelectbox>div>div>div {
        background-color: #FFFFFF;
    }
    </style>
""", unsafe_allow_html=True)

# ── Backend Storage Setup ────────────────────────────────────────────────────
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_module_for_andy(uploaded_file) -> str:
    """Takes a file uploaded in the browser and saves it for Andy to read."""
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def get_available_modules() -> list[str]:
    """Returns a list of PDF/PPTX files currently in the uploads folder."""
    if not os.path.exists(UPLOAD_DIR):
        return []
    return [f for f in os.listdir(UPLOAD_DIR) if f.endswith(('.pdf', '.pptx'))]

# ── Session State Initialization ─────────────────────────────────────────────
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "cards_queue" not in st.session_state:
    st.session_state.cards_queue = []
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "wrong_attempts_on_card" not in st.session_state:
    st.session_state.wrong_attempts_on_card = set() 
if "failed_cards_pool" not in st.session_state:
    st.session_state.failed_cards_pool = [] 
if "card_status" not in st.session_state:
    st.session_state.card_status = "unanswered" 

# ── App Navigation ───────────────────────────────────────────────────────────
st.sidebar.title("🤖 Andy's Dashboard")
app_mode = st.sidebar.radio("Navigation", ["📚 Study Dashboard", "✨ Create New Reviewer"])

st.sidebar.divider()

# =============================================================================
# MODE 1: CREATE NEW REVIEWER (ANDY'S WORKSHOP)
# =============================================================================
if app_mode == "✨ Create New Reviewer":
    st.title("✨ Ask Andy to Build a Reviewer")
    st.write("Upload your modules, set your parameters, and Andy will generate situational flashcards to test your knowledge.")

    # 1. File Upload Section
    st.subheader("1. Upload Modules")
    uploaded_files = st.file_uploader("Upload PDF or PPTX files", type=['pdf', 'pptx'], accept_multiple_files=True)
    
    if uploaded_files:
        for file in uploaded_files:
            save_module_for_andy(file)
        st.success(f"Successfully saved {len(uploaded_files)} file(s) to Andy's workspace!")

    # 2. Configuration Form
    st.subheader("2. Configure Reviewer")
    available_files = get_available_modules()
    
    if not available_files:
        st.info("Upload some files above to get started.")
    else:
        with st.form("generation_form"):
            selected_files = st.multiselect("Select modules to include in this reviewer:", available_files)
            deck_name = st.text_input("Reviewer Name (e.g., Midterm Coverage)")
            subject_name = st.text_input("Subject (e.g., Computer Science)")
            target_questions = st.slider("How many situational questions do you want?", min_value=5, max_value=50, value=15, step=5)
            
            submit_button = st.form_submit_button("🚀 Generate with Andy")
            
            if submit_button:
                if not selected_files:
                    st.error("Please select at least one module!")
                elif not deck_name or not subject_name:
                    st.error("Please fill out the Reviewer Name and Subject.")
                else:
                    with st.spinner("Andy is reading your modules and crafting tricky scenarios... This might take a minute!"):
                        # Call the backend function!
                        new_deck_id = generate_custom_deck(
                            selected_files=selected_files,
                            deck_name=deck_name,
                            subject=subject_name,
                            total_questions=target_questions
                        )
                        
                        if new_deck_id:
                            st.success(f"Done! Andy created '{deck_name}' with {target_questions} questions. Head over to the Study Dashboard to try it out!")
                            st.balloons()
                        else:
                            st.error("Andy couldn't generate the deck. Check the terminal for errors (the PDF might be empty or unreadable).")

# =============================================================================
# MODE 2: STUDY DASHBOARD (YOUR ORIGINAL CODE)
# =============================================================================
elif app_mode == "📚 Study Dashboard":
    st.title("📚 Study Dashboard")
    decks = db.get_decks()

    if not decks:
        st.warning("No decks found. Head over to 'Create New Reviewer' to have Andy make one!")
    else:
        deck_options = {d[0]: f"{d[1]} ({d[3]})" for d in decks}
        selected_deck_id = st.selectbox("Select a Reviewer Deck", options=list(deck_options.keys()), format_func=lambda x: deck_options[x])

        if st.button("Launch Reviewer Session"):
            raw_cards = db.get_cards_for_deck(selected_deck_id)
            
            if not raw_cards:
                st.error("This deck has no questions!")
            else:
                st.session_state.cards_queue = []
                for c in raw_cards:
                    st.session_state.cards_queue.append({
                        "id": c[0],
                        "type": c[2],
                        "question": c[3],
                        "correct_answer": c[4],
                        "options": json.loads(c[5]) if c[5] else []
                    })
                    
                st.session_state.current_index = 0
                st.session_state.wrong_attempts_on_card = set()
                st.session_state.failed_cards_pool = []
                st.session_state.card_status = "unanswered"
                st.session_state.quiz_started = True

    st.divider()

    if st.session_state.quiz_started and st.session_state.current_index < len(st.session_state.cards_queue):
        current_card = st.session_state.cards_queue[st.session_state.current_index]
        
        st.write(f"### Question {st.session_state.current_index + 1} of {len(st.session_state.cards_queue)}")
        st.info(current_card["question"])
        
        if current_card["type"] == "multiple_choice":
            options = current_card["options"]
            correct = current_card["correct_answer"]
            
            for option in options:
                if option in st.session_state.wrong_attempts_on_card:
                    st.button(f"❌ {option} (Incorrect Try Again)", key=option, disabled=True)
                else:
                    if st.button(option, key=option):
                        if option == correct:
                            st.success("🎯 Correct!")
                            st.session_state.current_index += 1
                            st.session_state.wrong_attempts_on_card.clear()
                            st.rerun()
                        else:
                            st.session_state.wrong_attempts_on_card.add(option)
                            if current_card not in st.session_state.failed_cards_pool:
                                st.session_state.failed_cards_pool.append(current_card)
                                db.update_card_miss_count(current_card["id"]) 
                            st.warning("That's not quite right. You have one more shot!")
                            st.rerun()

    elif st.session_state.quiz_started:
        st.balloons()
        st.success("🏁 You've cleared this reviewing round!")
        
        if st.session_state.failed_cards_pool:
            st.write(f"You have {len(st.session_state.failed_cards_pool)} questions that weren't fully aced on the first try.")
            if st.button("🔴 Focus Review: Practice Missed Questions Only"):
                st.session_state.cards_queue = list(st.session_state.failed_cards_pool)
                st.session_state.failed_cards_pool = []
                st.session_state.current_index = 0
                st.session_state.wrong_attempts_on_card.clear()
                st.rerun()
                
        if st.button("🔄 Reflash Entire Reviewer Deck"):
            st.session_state.current_index = 0
            st.session_state.wrong_attempts_on_card.clear()
            st.session_state.failed_cards_pool = []
            st.rerun()