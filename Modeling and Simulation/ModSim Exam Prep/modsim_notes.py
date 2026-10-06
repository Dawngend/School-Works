"""Build the CS0019 Modules 1-3 written reviewer from the supplied slides."""
from pathlib import Path
import sys
from xml.sax.saxutils import escape

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
LIB = ROOT.parent / "Network and Communications 2" / "DEVASC M3-M4 Exam Prep"
sys.path.insert(0, str(LIB))
from notes_lib import Notes


def save_pdf(doc, path):
    """Export the generated Word content when Office COM is unavailable."""
    from docx.oxml.ns import qn
    from docx.table import Table as WordTable
    from docx.text.paragraph import Paragraph as WordParagraph
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, PageBreak

    font_dir = Path("C:/Windows/Fonts")
    for name, filename in (("TimesNewRoman", "times.ttf"), ("TimesNewRoman-Bold", "timesbd.ttf"),
                           ("TimesNewRoman-Italic", "timesi.ttf")):
        pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
    pdfmetrics.registerFontFamily("TimesNewRoman", normal="TimesNewRoman",
                                  bold="TimesNewRoman-Bold", italic="TimesNewRoman-Italic")
    styles = {
        "Normal": ParagraphStyle("Body", fontName="TimesNewRoman", fontSize=12, leading=15, spaceAfter=6),
        "Title": ParagraphStyle("Title", fontName="TimesNewRoman-Bold", fontSize=20, leading=24, spaceAfter=12, alignment=TA_CENTER),
        "Heading 1": ParagraphStyle("H1", fontName="TimesNewRoman-Bold", fontSize=15, leading=19, spaceBefore=15, spaceAfter=7, keepWithNext=True),
        "Heading 2": ParagraphStyle("H2", fontName="TimesNewRoman-Bold", fontSize=13, leading=17, spaceBefore=11, spaceAfter=5, keepWithNext=True),
        "Heading 3": ParagraphStyle("H3", fontName="TimesNewRoman-Bold", fontSize=12, leading=15, spaceBefore=8, spaceAfter=4, keepWithNext=True),
    }
    flow = []
    list_number = 0
    for child in doc.element.body.iterchildren():
        if child.tag == qn("w:p"):
            p = WordParagraph(child, doc)
            if child.xpath(".//w:br[@w:type='page']"):
                flow.append(PageBreak())
                continue
            content = "".join(("<b>" if r.bold else "") + escape(r.text or "") +
                              ("</b>" if r.bold else "") for r in p.runs)
            if not content.strip():
                continue
            style = styles.get(p.style.name, styles["Normal"])
            if p.style.name.startswith("List"):
                if p.style.name == "List Number":
                    list_number += 1
                    content = f"{list_number}. " + content
                else:
                    content = "• " + content
            elif p.style.name not in ("Normal",):
                list_number = 0
            flow.append(Paragraph(content, style))
        elif child.tag == qn("w:tbl"):
            table = WordTable(child, doc)
            rows = []
            for row in table.rows:
                cells = []
                for cell in row.cells:
                    value = "<br/>".join(escape(p.text) for p in cell.paragraphs if p.text)
                    cells.append(Paragraph(value, styles["Normal"]))
                rows.append(cells)
            if not rows:
                continue
            cols = len(rows[0])
            raw_widths = [cell.width.twips if cell.width else 1 for cell in table.rows[0].cells]
            total_width = sum(raw_widths)
            widths = [468 * width / total_width for width in raw_widths]
            t = Table(rows, colWidths=widths, repeatRows=1, hAlign="LEFT")
            is_watch = table.rows[0].cells[0].text.startswith("Watch Out")
            is_memory = table.rows[0].cells[0].text.startswith("Memory Aid")
            fill = "#FDECEA" if is_watch else "#E8F0FE" if is_memory else "#E8EEF5"
            t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), .35, colors.grey),
                                   ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                   ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(fill)),
                                   ("LEFTPADDING", (0, 0), (-1, -1), 4),
                                   ("RIGHTPADDING", (0, 0), (-1, -1), 4)]))
            flow.extend((t, Spacer(1, 6)))
    SimpleDocTemplate(str(path), pagesize=letter, leftMargin=72, rightMargin=72,
                      topMargin=72, bottomMargin=72).build(flow)


def add(n, heading, paragraphs=(), bullets=()):
    n.h2(heading)
    for paragraph in paragraphs:
        n.p(paragraph)
    if bullets:
        n.bullets(bullets)


def build():
    n = Notes("CS0019 Modeling and Simulation: Midterm Reviewer", "Dawn Andrei Pamesa | Modules 1 to 3 | Friday, October 9, 11 AM | Canvas")
    n.p("Use the definitions, contrasts, formulas, worked examples, and MATLAB syntax below for written review. Source: supplied M1, M2, and M3 slide text, picture-slide notes, and M3 slide PDF.")
    n.h1("Module 1: Introduction to Modeling and Simulation")
    add(n,"Core Concepts",[
        "**Modeling and simulation (M&S)** is a problem-based discipline for repeated hypothesis testing. Its four precepts are **modeling, simulation, visualization, and analysis**. A system is interacting elements with a common purpose; elements may include people, hardware, software, facilities, policies, and documents.",
        "A **model** is a physical, mathematical, or logical representation of a system, entity, phenomenon, or process. **Simulation** operates or imitates a system through a model over time or space. **M&S** builds a model, executes it, and analyzes the resulting performance data for decisions. A system is the subject; a model represents it; simulation runs it.",
        "Study a system through the actual system or a model. A model may be physical or mathematical; a mathematical model may yield an analytical solution or require simulation. Modelers quantify behavior, support design/control/use, and evaluate performance."
    ])
    n.table(["System Type","Meaning / Example"],[
        ["Physical / notional","Physical exists (factory line); notional is a concept for something not yet existing."],
        ["Discrete / continuous","Discrete state changes at separate instants (factory); continuous state changes smoothly over time (aircraft)."],
        ["Open / closed","Open has exogenous activities from outside the boundary; closed has none."],
        ["Sampled-data","Underlying system is continuous, but observations are available only at discrete times."]],[1.7,4.8])
    add(n,"System Components And Boundary",[
        "An **entity** is an object of interest; an **attribute** is its property; an **activity** is a process changing the system. The **state** collects relevant entity, attribute, and activity values at one time. The boundary determines what is internal. **Endogenous** activities occur inside it; **exogenous** activities originate outside it. **Deterministic** activity output is fully determined by input; **stochastic** activity output includes randomness."
    ])
    n.table(["System","Entity","Attribute","Activity"],[
        ["Supermarket","Customers","Shopping list","Checking out"],["Bank","Customers","Account number, balance, credit status","Deposits, withdrawals"],["Communication","Messages","Length, priority","Transmitting"],["Rapid rail","Passengers","Origin, destination","Traveling"],["Traffic","Cars","Speed, distance","Driving"]],[1.2,1.2,2.1,2.0])
    n.table(["System","Endogenous","Exogenous"],[
        ["Supermarket","Purchasing and checkout","Customer arrivals"],["Supermarket parking","Arrival of customers in supermarket","Arrival of cars"]],[1.6,2.45,2.45])
    n.memory("Boundary test: ask whether an activity originates inside the chosen system. The same real-world event can be classified differently if the boundary changes.")
    add(n,"Why And How To Model",[
        "Model when the system is inaccessible, dangerous or unacceptable to engage, or does not yet exist. First establish structure by setting the boundary and identifying entities, attributes, and activities. Then supply attribute values and define activity relationships.",
        "**Model type tree:** physical models may be static or dynamic. Mathematical models may be static or dynamic; either may be addressed analytically or numerically, and dynamic numerical models lead to system simulation. A **static** model has no time evolution; a **dynamic** model changes with time.",
        "**Principles:** block building represents interconnected input-output parts; relevance includes only what affects the question; accuracy uses correct information; aggregation groups individual entities into larger units."
    ])
    n.table(["Classification","First Case","Second Case"],[
        ["Static / dynamic","Snapshot without time progression","State evolves over time"],["Deterministic / stochastic","Same input produces unique output","Random inputs or outputs"],["Continuous / discrete","State changes smoothly","State changes at events"]],[1.6,2.45,2.45])
    add(n,"Simulation History And Process",[
        "**Timeline:** 1940s Monte Carlo and neutron scattering; 1960s special-purpose languages such as SIMSCRIPT; 1970s mathematical foundations; 1980s PC software, GUIs, object orientation; 1990s web simulation, animation, optimization, and Markov-chain Monte Carlo.",
        "**Process:** define the problem, identify important variables, construct the simulation model, set values to test, run it, examine results, and choose a course of action. Repeat when results suggest model changes."
    ])
    n.h3("Ten Steps In Simulation And Model Building")
    n.numbered(["Define the goal.","Use a suitable mix of skills.","Involve the end user.","Choose suitable tools.","Set an appropriate level of detail.","Collect input data early.","Document the model.","Plan verification: does the implementation give the right answers for the model?","Plan validation: does the model answer the right questions about reality?","Analyze output statistically."])
    n.p("**Development cycle:** model (modeling technology) -> implement/code (development technology) -> execute simulation (computation) -> results -> analyze insight (data/information) -> revise model. Related disciplines: probability/statistics for random inputs and output, analysis/operations research, visualization, human factors, and project management.")
    n.table(["Method","Best Fit","Result / Limitation"],[
        ["Analytical","Simple tractable model; algebra, calculus, probability","General or exact result under assumptions; may produce difficult integrals."],
        ["Simulation","Complex or nonlinear model with delays, constraints, or many interactions","Numerical, scenario-specific estimates; requires runs, validation, and output analysis."]],[1.3,2.6,2.6])
    add(n,"Strengths, Limits, And Paradigms",[
        "**Advantages:** explore system behavior without disturbing it; test changes and configurations; expose bottlenecks; diagnose interactions; compare policies. **Disadvantages:** model design needs expertise; data and development take time and money; stochastic results vary; interpreting results requires care.",
        "**Monte Carlo:** repeatedly sample input distributions and compute output distributions. **Continuous simulation:** state varies continuously in time, often through differential equations. **Discrete-event simulation (DES):** state changes at event times; clock advances to events and queuing models are common. Hybrid, real-time, and web-based simulation are other forms.",
        "**Fidelity** is closeness of behavior to reality; **resolution** is degree of represented detail; **scale** is size of the represented scenario. A model can cover a large scale but omit fine detail. Slides compare chess, flight simulators, WoW, Halo, Doom, and WarSim along these dimensions.",
        "**Modeling methods:** physics-based derives equations from physical laws; finite element divides a complex object into elements; data-based fits observed data; agent-based models interacting agents; aggregate combines small entities; hybrid combines paradigms. Other forms on the slides include Markov chains, finite-state automata, particle systems, queueing models, bond graphs, and Petri nets."
    ])
    n.table(["Simulation","Participants","Systems"],[["Live","Real","Real"],["Virtual","Real","Simulated"],["Constructive","Simulated","Simulated"]],[1.7,2.4,2.4])
    n.p("Applications: training, analysis, experimentation, engineering, and acquisition. Randomness distinguishes deterministic simulations (unique output for given input) from stochastic ones (random input and output). Domains named in the slides include military, transportation, decision support, games for learning, and medicine. Other examples include manufacturing, networks, computer systems, hospitals, inventory, and finance.")
    n.h2("MATLAB Basics")
    n.p("MATLAB means Matrix Laboratory. Each variable is an array; `mynum = 6` is a 1 x 1 array. Names begin with a letter and then use letters, digits, or underscore; names are case-sensitive, length is limited by `namelengthmax`, and keywords are forbidden. Avoid shadowing built-in function names. `who` lists names, `whos` adds type/size details, `clear` clears all variables, and `clear x` clears x.")
    n.table(["Class / Control","Rule / Example"],[
        ["Numeric","Default is double; single and signed/unsigned int8 through int64/uint64 exist. int8 range = -128 to 127; intmin('int8'), intmax('int8')."],
        ["Other classes","char for character arrays; logical for true/false. Cast with class functions."],
        ["Display","format short (default) or long changes displayed digits; loose/compact changes spacing; 2e4 = 20000."],
        ["Special values","pi, i/j (imaginary unit), Inf, NaN. A user variable named i or j can overwrite the built-in meaning."],
        ["ASCII","double('a') = 97; char(97) = 'a'; char('abcd'+1) = 'bcde'."]],[1.4,5.1])
    n.p("Arithmetic: +, -, *, /, \\, ^; relational: <, <=, >, >=, ==, ~=; logical: &&, ||, ~, xor. MATLAB precedence follows parentheses, powers, unary negation, multiplication/division, addition/subtraction, relations, AND, OR, assignment. Use parentheses when uncertain. `fix`, `floor`, `ceil`, `round`, `mod`, `rem`, `sign`, `sqrt`, `nthroot`, `log` (natural), `log2`, `log10`, `exp`, `sin` (radians), and `sind` (degrees) are slide functions.")
    n.h3("Vectors, Matrices, And Indexing")
    n.p("A scalar is 1 x 1; a column vector may be 3 x 1, a row vector 1 x 4, a matrix 2 x 3. `v = [1 2 3 4]` is a row vector; `1:5` gives [1 2 3 4 5]; `1:2:9` gives [1 3 5 7 9]. Semicolons separate rows: `[1;2;3]`. Apostrophe transposes a real row vector into a column. Matrix rows must have equal lengths.")
    n.p("MATLAB indices start at 1. `v(2)` selects element 2; `v(2:3)` selects a slice; `mat(2,3)` selects row 2, column 3; `mat(1:2,2:3)` selects a block. Assignment such as `b(2)=11` changes an element. `length(v)` gives vector length; for a matrix it gives its largest dimension. `[r,c]=size(mat)` gives row/column counts; `numel(mat)` gives total elements.")
    n.table(["Command","Meaning / Slide Example"],[
        ["reshape(mat,2,6)","Reshapes a 3 x 4 matrix to 2 x 6, preserving columnwise element order."],
        ["fliplr / flipud / rot90","Reverse columns / reverse rows / rotate 90 degrees counterclockwise."],
        ["repmat(intmat,3,2)","Tiles a matrix 3 times vertically and 2 times horizontally."],
        ["evec=[]","Empty vector: length 0. `evec=[evec 4]` appends 4; `v(2)=[]` deletes vector element 2."],
        ["min / sum / max / prod","Reduce a vector; for a matrix operate on each column by default. `max(mat')` finds row maxima in a row vector; `max(mat,[],2)` returns column of row maxima."],
        ["cumsum / cumprod","cumsum(1:5) = [1 3 6 10 15]; cumprod(1:5) = [1 2 6 24 120]."]],[2.25,4.25])
    n.p("**Scalar versus array operations:** `v*3` and `v/2` scale each element; `v1+v2` adds corresponding elements. For elementwise multiplication, division, and power use `.*`, `./`, and `.^`. Ordinary `*` performs matrix multiplication: A (2 x 3) times B (3 x 4) yields C (2 x 4). Slide output C = [35 46 17 19; 9 22 20 5]. `det([1 2 3;2 3 4;1 2 5]) = -2`.")
    n.watch("The dot changes multiplication-based operators into elementwise operations. `A*B` requires inner dimensions to agree; `A.*B` requires compatible elementwise sizes. A row or column transpose changes dimensions.")
    n.pagebreak()
    n.h1("Module 2: Discrete Event Simulation")
    add(n,"Sets, Functions, And Probability",[
        "A **set** is a collection without duplicate elements; the empty set { } has no elements. A subset contains only elements of a larger set. Union includes elements in either set; intersection includes elements in both; difference removes the second set; complement includes elements in the sample space outside the set. Finite sets have a terminating count; countable sets can be paired with positive integers.",
        "**Worked set example:** A={2,4,10}, B={4,6,8,10}, S={2,4,6,8,10,12}. A union B ={2,4,6,8,10}; A∩B={4,10}; A−B={2}; B−A={6,8}; Aᶜ={6,8,12}.",
        "A function maps each domain element to one codomain element. Its **range** is the outputs actually reached. It is **onto** if range = codomain and **one-to-one** if different inputs have different outputs. An inverse exists when both hold. For f(x)=mx+b over real numbers, m≠0 gives inverse f⁻¹(y)=(y−b)/m; m=0 is constant and has no inverse."
    ])
    n.p("A **probability space (S,A,P)** has a sample space S, a sigma algebra A of events, and a probability measure P. An event is a subset of S. A contains S and is closed under complements and countable unions (therefore intersections). For k outcomes, the full power set has **2^k** events; the slide's finite example uses this full sigma algebra. P maps events to [0,1], P(S)=1, and probabilities add for disjoint events.")
    n.table(["Three-Sided Die Event","Probability"],[["{ } (empty set)","0"],["{B}","1/6"],["{C}","1/3"],["{D}","1/2"],["{B,C}","1/2"],["{B,D}","2/3"],["{C,D}","5/6"],["S={B,C,D}","1"]],[3.6,2.9])
    n.p("A **random variable** X maps sample outcomes to real numbers, with {X≤x} an event for each x. Its **CDF** F(x)=P(X≤x), a nondecreasing step function for the die example. For a continuous X, the **PDF** f(x)=dF/dx is nonnegative, integrates to 1, and P(x1<X≤x2)=∫[x1,x2]f(x)dx. A discrete variable has probability masses, not an ordinary continuous density.")
    n.table(["Distribution","Parameters And Use"],[
        ["Uniform(a,b)","Minimum a, maximum b, a<b; values equally likely across a finite interval. Density 1/(b−a)."],
        ["Triangular(a,m,b)","Minimum a, most likely m, maximum b, a<m<b; use when approximate bounds and mode are known."],
        ["Exponential(m)","Mean interarrival time m>0; rate λ=1/m. Density λexp(−λx) for x≥0; P(X>x)=exp(−λx)."],
        ["Normal(m,σ)","Mean m, standard deviation σ>0; variability around an average and sums of many influences."]],[2.0,4.5])
    n.watch("For the exponential distribution, λexp(−λx) is the normalized density. The slide's displayed formula omits λ; its survival probability exp(−λx) is correct.")
    add(n,"Random Variates And Data Models",[
        "A **random variate** is a sampled value from a chosen distribution. Generate a pseudorandom uniform number U in [0,1), then transform it to the desired distribution. The linear congruential generator is Z(k+1)=(aZ(k)+c) mod m and U(k)=Z(k)/m, where Z(0) is the seed. The period is at most m; a full cycle has period m.",
        "**Full-cycle conditions:** c and m are relatively prime; every prime factor of m divides a−1; if 4 divides m, then 4 divides a−1. Slide example a=1, c=3, m=20, seed 2 gives Z: 2, 5, 8, 11, 14, 17, 0, ... and a full 20-value cycle because gcd(3,20)=1 and a−1=0 satisfies the divisibility conditions.",
        "**Structural modeling** defines entities, locations, resources, processes, and logic. **Data modeling** supplies quantitative values such as interarrival and service times, resource schedules, failures, and travel times. Simple input data may use samples, empirical distributions, or theoretical distributions; hard cases include no data, multimodal, correlated, or nonstationary data."
    ])
    n.table(["Input Choice","Advantage","Disadvantage"],[
        ["Direct sample","Only observed, legal values","Rare legal values may be missing; storage access and many draws can be slow."],
        ["Empirical distribution","Unlimited draws matching the observed sample","Cannot produce unobserved rare extremes."],
        ["Theoretical distribution","Smooths small-sample noise; efficient draws","Fitting parameters takes effort; fit may be poor."]],[1.5,2.35,2.65])
    n.p("**Output data analysis** turns simulation traces into performance measures. Estimate means and confidence intervals, and account for stochastic variation before comparing scenarios.")
    add(n,"DES Mechanics",[
        "**DES** represents a dynamic system whose state changes instantaneously at separate event times. An **entity** moves through the system; an **attribute** records its individual data; a **resource** serves it with finite capacity; a **queue** holds it when service is unavailable; an **event** changes the state. Resource utilization = busy time / total observed time.",
        "Five software features on the slides: entities, relationships, simulation executive, random-number generator, and results/statistics. The **simulation clock** is modeled time. The **future event list** orders scheduled events; state variables describe the current system; statistical accumulators collect performance data. Initialization sets the initial state; a timing routine chooses the next event; the event routine updates state; a random-variate library supplies draws; the main program coordinates; the report generator summarizes.",
        "**Flowchart:** main program -> initialization -> timing (select next event) -> event routine (possibly draw from distribution library) -> termination test -> repeat timing if no, or report if yes. **Fixed-increment/time slicing** advances by constant Δt and may shift events to grid times. **Next-event** jumps to the earliest scheduled event and skips inactive time."
    ])
    n.memory("At each DES event: advance the clock, update state, schedule any new events, and update counters. The clock does not tick through quiet periods under next-event advance.")
    add(n,"Queueing Systems",[
        "Arrival variation and service-time variation create lines. Basic elements are customers/entities, server(s), and waiting queue(s). Interarrival time is the interval between arrivals; service time is time at the resource. A queue discipline determines who is served next: FIFO/FCFS, LIFO/LCFS, priority, SIRO (random order), or shortest processing time.",
        "A customer may **jockey** by switching lines, **renege** by leaving after joining, **balk** by declining to join, or **faff** by delaying after checkout while gathering belongings. An analytical queue model is tractable for simpler systems; simulation handles complex multistation behavior. Balance service cost against customer waiting cost. The slide coffee-shop example minimizes total cost at **$320 with two baristas**.",
        "Key parameters: arrival rate, service rate, number of servers, optional maximum queue length, and optional source population. Four structures: single server/single phase (ATM), single server/multiple phases (Chipotle), multiple servers/single phase (shared line), and multiple servers/multiple phases (laundromat)."
    ])
    n.watch("**LIFO** means Last In, First Out (slide says 'FIFO - Last in, First Out'). FIFO means First In, First Out.")
    n.h3("Single-Server Formulas")
    n.p("For customer i: arrival Aᵢ = prior arrival + interarrival; service begins Bᵢ=max(Aᵢ,Eᵢ₋₁); waiting Wᵢ=Bᵢ−Aᵢ; service ends Eᵢ=Bᵢ+Sᵢ; time in system Tᵢ=Eᵢ−Aᵢ=Wᵢ+Sᵢ; server idle before i is max(0,Aᵢ−Eᵢ₋₁). For the first arrival at time 0, B₁=0.")
    n.watch("**Waiting in queue = service begins − arrival** (slide says 'arrival − service begins'). This must be nonnegative. Server idle time is also clamped at zero.")
    n.table(["Customer","IAT","Arrival","Service","Begin","Wait","End","System","Idle"],[
        ["1","-","0","2","0","0","2","2","0"],["2","4","4","3","4","0","7","3","2"],["3","1","5","1","7","2","8","3","0"],["4","4","9","4","9","0","13","4","1"],["5","2","11","2","13","2","15","4","0"],["6","4","15","3","15","0","18","3","0"],["Total","15","","15","","4","","19","3"]],[0.8,0.55,0.75,0.65,0.65,0.55,0.55,0.75,0.65])
    n.p("Customer 3: B₃=max(5,7)=7, W₃=7−5=2, E₃=7+1=8, T₃=8−5=3. Over the six customers, average wait = 4/6 minute and average system time = 19/6 minutes. The server is idle 3 minutes before the last departure at t=18.")
    n.pagebreak()
    n.h1("Module 3: Modeling Continuous Systems")
    add(n,"Continuous-System Framework",[
        "A **continuous system** has state variables that evolve continuously with time. It can be represented as input x(t) -> system -> output y(t). For a reservoir, the stored quantity q changes according to dq/dt=x and output y=q. Examples on the slides span dams and tunnels, missile and aircraft systems, logistics, and business planning. Some logistics examples are naturally discrete-event and require a matching model choice.",
        "Mathematical classes on the slides: first-order ODEs (predator-prey), second-order ODEs (F=ma, orbits, oscillators, ballistics, RLC circuits), and second-order PDEs (listed but not treated). Modeling strategy: understand the system's physics and turn it into quantitative equations; then choose a numerical solution method.",
        "**State variables** collectively contain enough information to predict relevant future behavior at the required accuracy. Examples: position, velocity, mass, angle, current, voltage. **State equations** describe time derivatives of state. **Output equations** map state to quantities users need. The orbital example uses three-dimensional position and velocity as the state vector."
    ])
    n.h2("Predator-Prey Dynamics")
    n.p("The cycle: prey increase -> predators have more food -> predators increase -> prey decline -> predators starve -> predators decline -> prey recover. Let x be prey and y predators. Kolmogorov form is dx/dt=x f(x,y), dy/dt=y g(x,y). The slide's Lotka-Volterra rates are f=b−py and g=rx−d, so dx/dt=x(b−py), dy/dt=y(rx−d). Increasing predators lowers prey growth; increasing prey raises predator growth. With b=r=d=p=1, the slide plots closed orbits for different initial conditions.")
    n.watch("The slide's printed conserved quantity for general b,p,r,d is inconsistent. From the displayed rate equations, a conserved expression is **r x − d ln x + p y − b ln y**. For b=r=d=p=1 this is x−ln x+y−ln y, up to sign and an additive constant.")
    n.h2("Numerical Methods")
    n.p("Most coupled state equations have no simple closed-form solution. **Euler:** for dx/dt=f(t,x), xₙ₊₁≈xₙ+h f(tₙ,xₙ). It follows the tangent slope over a short step h. **Midpoint Runge-Kutta (RK2) shown in the slides:** tmid=tₙ+h/2, xmid=xₙ+(h/2)f(tₙ,xₙ), then xₙ₊₁=xₙ+h f(tmid,xmid). The midpoint slope usually improves on forward Euler for a similar step.")
    n.h2("MATLAB Scripts, Functions, And Input/Output")
    n.p("Both scripts and functions use .m files. A **script** runs commands in the workspace with no input/output argument list. A **function** accepts arguments, returns output, and keeps internal variables local. Create or open a file with `edit filename.m`; the slides show making a directory, changing into it, and running a script. A radius-5 circle script computes area `pi*5^2 = 78.5398`.")
    n.table(["Command / Code","Meaning"],[
        ["input('Enter a number: ')","Reads an evaluated numeric expression; assign it to a variable."],
        ["input('Enter a string: ','s')","Reads text literally. Empty Enter gives empty char input; leading spaces are retained."],
        ["disp(x)","Displays a value without its variable name."],
        ["fprintf('...%d...\\n',x)","Formatted text; %d integer, %f fixed decimal, %e scientific, %g compact, %s string; \\n newline and \\t tab."],
        ["fscanf(...) / format","Formatted input / numeric display mode. `format short`, `long`, `compact`, `loose` control appearance."],
        [";","Suppresses automatic command-window output."]],[2.8,3.7])
    n.p("Slide examples: `fprintf('%s will be %d this year.\\n','Alice',12)` prints 'Alice will be 12 this year.' `disp(4^3)` displays 64. With x=5 and y=9, the input script computes z1=14, z2=-4, z3=45, and z4=7. Use `%f` rather than `%d` for a potentially fractional average.")
    n.p("To print vectors, `fprintf('%d\\n',vec)` writes one element per line; `fprintf('%d ',vec)` writes across a line. MATLAB feeds matrix elements to `fprintf` column by column, so choose format and transpose deliberately. Slide vector `[2 3 4 5]` appears as four lines with newline formatting or `2 3 4 5` with spaced formatting.")
    n.h2("Plotting")
    n.p("Define x values, calculate y=f(x) elementwise, and call `plot(x,y)`. `xlabel`, `ylabel`, `title`, `grid on`, `axis equal`, `axis square`, `axis([xmin xmax ymin ymax])`, `hold on`, `legend`, `subplot`, and `figure` control presentation. The slide's plot commands also include `bar`, `loglog`, `semilogx`, `semilogy`, `stairs`, and `stem`.")
    n.p("**LineSpec** combines optional color, line style, and marker. Colors: b blue, c cyan, g green, k black, m magenta, r red, w white, y yellow. Styles: `-` solid, `--` dashed, `:` dotted, `-.` dash-dot. Markers include `o` circle, `+` plus, `*` star, `.` point, `x` cross, `s` square, `d` diamond, `^` upward triangle, and `p` pentagram. Example `plot(x,y,'r*')` shows red stars.")
    n.p("Slide plot examples: `plot(11,48,'r*')` marks one time/temperature point; `x=1:6; y=[1 5 3 9 11 8]; plot(x,y)` makes a line. `subplot(2,2,1)` selects the first tile of a 2 x 2 grid; `figure` opens another window; `plot(x,y1,x,y2)` draws both curves. The sin/cos example sets x from 0 to 2π, y1=sin(x), y2=cos(x), then adds legend and labels. The final example plots `exp(-1.5*x).*sin(10*x)` and `exp(-2*x).*sin(10*x)` in two subplots.")
    n.watch("Use `.*`, `./`, and `.^` in vector-valued function formulas. `axis equal` gives equal unit scale, while `axis square` gives a square plotting box.")
    n.h2("User-Defined Functions")
    n.p("A file `calcarea.m` can contain `function area = calcarea(rad)`, then `area = pi * rad * rad; end`. Calling `calcarea(5)` yields about 78.54. The slide's `conevol.m` returns `outarg=(pi/3)*radius.^2.*height`; `conevol(4,6.1)` gives about 102.2065, and the displayed `conevol(3,5.5)` value is 51.84 to two decimals. Function name and file name must match for the primary function.")
    n.h2("Selection And Loops")
    n.p("`if condition ... elseif condition ... else ... end` executes a matching branch. Slide example `a=100; if a<20 ... else fprintf('a is not less than 20\\n'); end` prints the else text. A sign test with `if x<0` prints Negative for negatives and Positive otherwise; zero belongs to the latter branch unless handled separately. The age example uses logical `&&` for ranges; ensure boundaries are exhaustive when adapting it.")
    n.p("Correct odd/even example: `x=input('Enter a number: '); if mod(x,2)==0; fprintf('Even number'); else; fprintf('Odd number'); end`. This is a valid MATLAB branch for integer x.")
    n.watch("Use `mod(x,2)` and print **Odd number** in the else branch (slide says `x % 2` and prints 'Even number' in both branches). In MATLAB `%` starts a comment.")
    n.p("`switch grade; case 'A'; ...; case 'B'; ...; otherwise; ...; end` selects a matching case. With grade='B', the slide prints 'Well done'. `menu('Pick a Pizza','Cheese','Sausage','Mushroom')` returns button number 1, 2, or 3; a switch then prints the chosen order. The slide's x=y=3 switch prints 'x and y are equal'.")
    n.p("`for v=1:10; disp(v); end` prints 1 through 10. `for v=[1 5 8 17]` visits those four values; `for v=1.0:-0.2:0.0` counts down by 0.2; another loop prints Hello ten times. `while condition; statements; end` repeats while the condition remains true. The slides' example increments a from 10 to 19; another breaks when a reaches 15; another uses `continue` to skip displaying 15. Ensure the body eventually changes the condition or uses `break`.")
    n.pagebreak()
    n.h1("One-Page Cram Sheet")
    n.p("**M1 core:** system = interacting parts; model = representation; simulation = run of model; M&S = build, execute, analyze. Four precepts: modeling, simulation, visualization, analysis. Entity/object; attribute/property; activity/change; state/snapshot. Open has exogenous activity; closed does not. Static/dynamic = no time/time; deterministic/stochastic = fixed/random; continuous/discrete = smooth/event changes.")
    n.p("**M1 process:** define goal and boundary -> model structure/data -> verify implementation -> validate model against purpose -> experiment -> statistically analyze output -> revise. Monte Carlo samples distributions; continuous uses differential equations; DES jumps between state-changing events. Fidelity = realism; resolution = detail; scale = scenario size. Live real/real; virtual real/simulated; constructive simulated/simulated.")
    n.p("**MATLAB M1:** indices start at 1; row `[1 2 3]`, column `[1;2;3]`, range `1:2:9`. `size` dimensions, `numel` elements, `length` largest dimension. `.*`, `./`, `.^` elementwise; `*` matrix product. `det(A)` determinant. `who`, `whos`, `clear`; `format short/long`; ASCII `double('a')=97`.")
    n.p("**M2 probability:** (S,A,P); full event set of k outcomes has 2^k subsets. CDF F(x)=P(X≤x); continuous PDF f=dF/dx, area=1. Uniform(bounds), triangular(bounds and mode), exponential(mean interarrival), normal(mean and SD). LCG Z(k+1)=(aZ(k)+c) mod m; U=Z/m. Full cycle: gcd(c,m)=1; prime factors of m divide a−1; if 4|m, 4|(a−1).")
    n.p("**M2 queue:** Bᵢ=max(Aᵢ,Eᵢ₋₁), Wᵢ=Bᵢ−Aᵢ, Eᵢ=Bᵢ+Sᵢ, Tᵢ=Eᵢ−Aᵢ, idle=max(0,Aᵢ−Eᵢ₋₁). Next-event advance jumps to earliest event. FIFO = first in, first out; LIFO = last in, first out. Six-customer totals: wait 4, time in system 19, idle 3 minutes.")
    n.p("**M3 continuous:** state equations determine derivatives, output equations calculate requested measurements. Lotka-Volterra: dx/dt=x(b−py), dy/dt=y(rx−d). Euler xnext≈x+h f(t,x); midpoint RK2 uses slope at t+h/2. MATLAB scripts use workspace; functions have local variables and return outputs. `input(...,'s')` reads text; `fprintf` uses %d, %f, %s and `\\n`; `plot(x,y,'r*')`; `if/elseif/else/end`, `switch/case/otherwise/end`, `for`, `while`; odd/even uses `mod(x,2)`.")
    output = ROOT / "PAMESA - ModSim Midterm Reviewer.docx"
    n.doc.save(output)
    save_pdf(n.doc, output.with_suffix(".pdf"))


if __name__ == "__main__":
    build()
