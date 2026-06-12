import streamlit as st
import random
import json
import database as db 

st.set_page_config(page_title="CS Academic Comeback Reviewer", layout="wide")

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

st.sidebar.title("📚 Study Dashboard")
decks = db.get_decks()

if not decks:
    st.sidebar.warning("No decks found. Please generate some using generator.py first!")
else:
    deck_options = {d[0]: f"{d[1]} ({d[3]})" for d in decks}
    selected_deck_id = st.sidebar.selectbox("Select a Reviewer Deck", options=list(deck_options.keys()), format_func=lambda x: deck_options[x])

    if st.sidebar.button("Launch Reviewer Session"):
        raw_cards = db.get_cards_for_deck(selected_deck_id)
        
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
else:
    st.subheader("Select a custom tracking deck from the sidebar to start studying.")