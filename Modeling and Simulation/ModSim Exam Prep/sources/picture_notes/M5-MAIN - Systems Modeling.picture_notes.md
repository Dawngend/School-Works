### Study Notes: Module 5 – Systems Modeling

---

#### [M5-MAIN - Systems Modeling-page-1.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-1.png)
- **Title:** Modeling and Simulation
- **Key Facts:** Course title slide with institutional branding (FEU Alabang, FEU Diliman, FEU Tech) and institutional motto (*"Technology Driven by Innovation"*).

---

#### [M5-MAIN - Systems Modeling-page-2.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-2.png)
- **Title:** MODULE 5: SYSTEMS MODELING
- **Key Facts:** Module introductory header slide.

---

#### [M5-MAIN - Systems Modeling-page-3.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-3.png)
- **Title:** SUBTOPIC 1: CONCEPTS ON SYSTEMS MODELING
- **Key Facts:** Topic divider for foundational concepts and classifications of system models.

---

#### [M5-MAIN - Systems Modeling-page-4.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-4.png)
- **Title:** OBJECTIVES
- **Key Facts:**
  - Understand system model concepts and categories.
  - Examine modeling types and underlying methodologies.
  - Identify modeling tools and formalisms.
  - Review operations research (OR) optimization methods.

---

#### [M5-MAIN - Systems Modeling-page-5.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-5.png)
- **Title:** Systems Modeling – System Model Types (Fishwick’s perspective on model types)
- **Key Facts:**
  - **Declarative Models:** State-event focused representations.
  - **Functional Models:** Directionally connected functional components expressing mathematical equation and variable relationships.
  - **Constraint Models:** Physics-based property balancing where non-directional physical relationships take precedence over directed dataflow.
  - **Spatial Models:** Multi-element representations where spatial coordinates/regions or the entities residing in them form the base elements.

---

#### [M5-MAIN - Systems Modeling-page-6.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-6.png)
- **Title:** Examples of Declarative Model
- **Key Facts & Values:**
  - **Finite State Automaton (FSA):** Easy Pass account system states:
    - States: `Start`, `Initializing accounts`, `Waiting for input`, `Checking accounts`, `Giving green light`, `Giving red light`, `Sending ticket`.
    - Event condition: `[Red light > 2 s]`.
  - **Queuing Simulation Model:** Toll booth scheduling:
    - Arrival event scheduled via exponential distribution: `expo(\mu)`.
    - Departure event scheduled via normal distribution: `norm(\mu, \sigma)`.
    - Event queue sample: `(A9, 2:15) (D1, 2:16)`.
  - **Markov Model & Revenue Loss Transition Matrix:**
    - States: $S_1, S_2, S_3, S_4, S_5$.
    - Transition matrix:
      $$\begin{matrix} & 1 & 2 & 3 & 4 & 5 \\ 1 & [0 & 1 & 0 & 0 & 0] \\ 2 & [0 & 0 & 0.8 & 0.2 & 0] \\ 3 & [0 & 0 & 0 & 0.3 & 0.7] \\ 4 & [1 & 0 & 0 & 0 & 0] \\ 5 & [1 & 0 & 0 & 0 & 0] \end{matrix}$$

---

#### [M5-MAIN - Systems Modeling-page-7.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-7.png)
- **Title:** Examples of Functional Model
- **Key Facts & Formulas:**
  - Vehicle deceleration under frictional force $F_f$, initial speed $v_0$, stopping distance $d$.
  - Block diagram layout:
    - Input deceleration parameter $a_f \rightarrow$ Constant block $[C] \rightarrow a$ ($a = dv/dt$).
    - Integrator $[\int]$ with initial condition $v_0 \rightarrow v$ ($v = dx/dt$).
    - Integrator $[\int] \rightarrow$ displacement position $x$.

---

#### [M5-MAIN - Systems Modeling-page-8.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-8.png)
- **Title:** Example of Constraint Model
- **Key Facts & Formulas:**
  - Pairs the block diagram from Slide 7 with an explicit energy conservation/work-energy constraint:
    $$\frac{1}{2}mv^2 = F_f d$$
  - Balances initial kinetic energy against mechanical work dissipated by friction over distance $d$.

---

#### [M5-MAIN - Systems Modeling-page-9.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-9.png)
- **Title:** Example of Spatial Model
- **Key Facts:**
  - Case: ISRO/SAC agricultural yield prediction via GIS/grid-based simulation.
  - Spatial input layers: *Weather surface*, *Soil Map*, *Wheat area*, *Crop Parameters*, *LAI Map* (Leaf Area Index), and *Phenology map*.
  - Execution pipeline: Crop Simulation Model $\rightarrow$ *Simulated Grid Yield* $\rightarrow$ *Area Weighted Yield* / *Yield map*.

---

#### [M5-MAIN - Systems Modeling-page-10.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-10.png)
- **Title:** Conceptual Models
- **Key Facts:**
  - Primary goal: Communicate high-level functionality and distinctive characteristics quickly.
  - High informality; low demand on mathematical rigor or implementation precision.
  - Typically conveyed in 1–2 descriptive paragraphs or schematic illustrations; the simplest form is a system drawing.

---

#### [M5-MAIN - Systems Modeling-page-11.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-11.png)
- **Title:** Examples of Conceptual Model
- **Key Facts & Numbers:**
  - Case study: Easy Pass (EP) electronic toll collection system.
  - Layout specs: 2-lane main highway maintaining posted speed limits via overhead RFID/sensors, coupled with a $500\text{ m}$ double bypass lane supporting 24-hour manual cash/card transactions.
  - Representations: Narrative textual description alongside overhead aerial and perspective layout sketches.

---

#### [M5-MAIN - Systems Modeling-page-12.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-12.png)
- **Title:** Multimodel (Hybrid Model)
- **Key Facts:**
  - Combines multiple distinct model types coupled into an interconnected network or graph.
  - Bridges different abstraction layers to evaluate questions that a single paradigm cannot address.
  - Fits complex multi-phase systems whose operational stages demand different formal modeling mechanics.

---

#### [M5-MAIN - Systems Modeling-page-13.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-13.png)
- **Title:** Concept Map
- **Key Facts:**
  - An informal directed graph where nodes (rectangles/ovals) represent components/entities and labeled arrows denote interaction verbs.
  - Easy Pass graph trace:
    - `Car` $\xrightarrow{\text{Triggers}}$ `Easy Pass sensor`
    - `Easy Pass sensor` $\xrightarrow{\text{Relies on}}$ `License plate camera`
    - `Easy Pass sensor` $\xrightarrow{\text{Compares with}}$ `Easy Pass account system`
    - `Easy Pass account system` $\xrightarrow{\text{Give green light to}}$ `Easy Pass driver`
    - `Easy Pass account system` $\xrightarrow{\text{Give red light to}}$ `Ordinary driver` $\xrightarrow{\text{Receives}}$ `Ticket`

---

#### [M5-MAIN - Systems Modeling-page-14.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-14.png)
- **Title:** Systems Modeling – Analysis of M&S (Tools for creating models: 1. Formal Modeling)
- **Key Facts:**
  - **Formalisms:** Strict mathematical rule sets governing modeling and simulation structures.
  - **Pros:** Unambiguous semantics, allows automated analysis, precise behavioral guarantees, bounds and constraints verification.
  - **Cons:** High complexity, difficult and time-consuming to design and implement.

---

#### [M5-MAIN - Systems Modeling-page-15.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-15.png)
- **Title:** Systems Modeling – Analysis of M&S (Tools for creating models: 2. Semiformal Modeling)
- **Key Facts:**
  - A practical middle ground: balances user-friendly visual modeling against some loss of formal rigor, while preserving analytical traceability.
  - Canonical standard: **UML** (Unified Modeling Language).
  - Primary UML diagram types listed:
    - Use Cases
    - Activity Diagrams
    - Class Diagrams
    - Sequence Diagrams
    - Statecharts

---

#### [M5-MAIN - Systems Modeling-page-16.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-16.png)
- **Title:** Systems Modeling – Analysis of M&S (Forms of Analysis: 1. Verification)
- **Key Facts:**
  - Definition: Verifying that the conceptual specification has been correctly translated into an executable model (*"building the model right"*).
  - Verification techniques:
    - *Automated debugging:* Flags syntax and basic logic issues (semantic analysis remains limited).
    - *Manual code reviews:* Collaborative peer walkthroughs.
    - *Stress testing:* Driving execution at extreme boundary conditions (min/max limits).

---

#### [M5-MAIN - Systems Modeling-page-17.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-17.png)
- **Title:** Systems Modeling – Analysis of M&S (Forms of Analysis: 2. Validation)
- **Key Facts:**
  - Definition: Ensuring the model sufficiently approximates the real-world system to provide credible answers (*"building the right model"*).
  - Validation approaches:
    - *Statistical comparison:* Quantifying deviations between simulated outputs and real target system data.
    - *Face validation:* Subjective evaluation by domain experts when the physical system is nonexistent or empirical data is unavailable.

---

#### [M5-MAIN - Systems Modeling-page-18.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-18.png)
- **Title:** Systems Modeling – OR Methods
- **Key Facts:**
  - Operations Research (OR) uses mathematical models to optimize system variables (maximizing gains, minimizing expenses).
  - 3-step optimization workflow:
    1. Formulate the problem
    2. Develop a mathematical model representing the system
    3. Solve the model to find the extrema (maxima/minima)
  - Method classes:
    - *Deterministic:* Linear Programming (LP) with objective functions and linear inequality constraints.
    - *Stochastic:* Markov chains, queuing theory.

---

#### [M5-MAIN - Systems Modeling-page-19.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-19.png)
- **Title:** Formative Assessment 6
- **Key Facts:** Directs students to Canvas for instructions on Formative Assessment 6.

---

#### [M5-MAIN - Systems Modeling-page-20.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-20.png)
- **Title:** Summative Assessment 5
- **Key Facts:** Directs students to Canvas for instructions on Summative Assessment 5.

---

#### [M5-MAIN - Systems Modeling-page-21.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-21.png)
- **Title:** References
- **Key Facts:**
  - Text: Sokolowski, John A. & Banks, Catherine M. (2010). *Modeling and Simulation Fundamentals Theoretical Underpinnings and Practical Domains*. John Wiley & Sons.

---

#### [M5-MAIN - Systems Modeling-page-22.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-22.png)
- **Title:** Introduction to MATLAB Simulink (Modeling and Simulation)
- **Key Facts:** Section transition slide marking the start of MATLAB Simulink coverage.

---

#### [M5-MAIN - Systems Modeling-page-23.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-23.png)
- **Title:** Subtopic 2: Introduction to MATLAB Simulink
- **Key Facts:** Subtopic header slide.

---

#### [M5-MAIN - Systems Modeling-page-24.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-24.png)
- **Title:** OBJECTIVES
- **Key Facts:** Objective: Know what Simulink is and understand its core engineering purpose.

---

#### [M5-MAIN - Systems Modeling-page-25.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-25.png)
- **Title:** What is Simulink
- **Key Facts:**
  - Environment: Graphical block editor, modular block libraries, and numerical solvers integrated with MATLAB®.
  - Core philosophy: *"Simulink is for Simulation"*.
  - Key applications: Pre-hardware prototyping, multi-domain system exploration, Hardware-in-the-Loop (HIL) testing, and scaled execution on multi-core desktops, clusters, and cloud infrastructure.

---

### Possible Slide Errors

1. **Slide 5 ([M5-MAIN - Systems Modeling-page-5.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-5.png)) — Duplicate Copy-Paste Definition under "Declarative Models":**
   - *Error:* Under section `1. Declarative Models`, the second bullet point reads: *"Describe a system using directionally connected components with mathematical relationships of equations and the variables that relate them."*
   - *Why it is wrong:* This is an accidental copy-paste identical to the definition under `2. Functional Models`. Declarative models in Fishwick's taxonomy are state- and event-driven formulations (such as state machines, Petri nets, or Markov chains), not functional signal/equation block diagrams.

2. **Slide 15 ([M5-MAIN - Systems Modeling-page-15.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-15.png)) — Awkward Double Negative / Phrasing Error:**
   - *Error:* The first bullet states: *"Semiformal representation methods are a trade-off that allows ease of use with less unambiguity, but with still a degree of analytic capability."*
   - *Why it is wrong:* *"Less unambiguity"* is a confusing double negative. Compared to formal methods (which are strictly unambiguous), semiformal methods trade away some rigor, meaning they have *more ambiguity* (or *less precision/rigor*).

3. **Slide 21 ([M5-MAIN - Systems Modeling-page-21.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M5-MAIN%20-%20Systems%20Modeling-page-21.png)) — Missing Punctuation in Book Citation:**
   - *Error:* The textbook title is printed as *"Modeling and Simulation Fundamentals Theoretical Underpinnings and Practical Domains"*.
   - *Why it is wrong:* It omits the colon separating the title from its subtitle (canonical title: *Modeling and Simulation Fundamentals: Theoretical Underpinnings and Practical Domains*).

### Study Notes

---

#### 1. `img/M5-MAIN - Systems Modeling-page-26.png`
* **Slide Title:** Simulink is for Every Project
* **Key Facts & Application Domains:**
  * Demonstrates the multi-domain modeling versatility of Simulink across eight engineering disciplines:
    * **Wireless Communications:** RF transmitter/receiver and spectrum/constellation visualizers.
    * **Power Electronics:** Circuit simulation with DC power source, switches/MOSFETs, and filters.
    * **Control Systems:** Feedback control loops, PID tuning, and aircraft/plant dynamics.
    * **Signal Processing:** Sigma-Delta A/D Conversion with time-domain and frequency-domain scopes.
    * **Autonomous Systems and Robotics:** Kinematic/dynamic modeling and robotic manipulator control.
    * **Advanced Driver Assistance Systems (ADAS):** Test bench, dashboard gauges, and automated vehicle driving logic.
    * **Digital Twins:** Multi-domain physical asset modeling (pumps/motors, fault injection).
    * **Artificial Intelligence:** Computer vision pipelines combining pre-processing (`Resize Image`), object detection (`Vehicle Detection (YOLOv2)`), lane finding (`Lane Detection`), coordinate extraction (`Detect Coordinates`), and video overlay (`Highlight Vehicles & Lanes`).

---

#### 2. `img/M5-MAIN - Systems Modeling-page-27.png`
* **Slide Title:** Simulink Start Page
* **Key Facts & Elements:**
  * **Top Navigation:** Tabs for `New`, `Examples`, and `Learn`, along with an `All` search field.
  * **Sidebar:**
    * `Recent`: Lists recently opened models (e.g., `/MATLAB Drive/scope1.slx`).
    * `Learn`: Quick access to tutorials like `Simulink Onramp`.
  * **Default Simulink Templates:**
    * `Blank Model`
    * `Blank Subsystem`
    * `Blank Library`
    * `Blank Project`
    * `Folder to Project`
    * `Code Generation`
    * `Digital Filter`
    * `Feedback Controller`
  * **Toolbox Categories Available:** Audio Toolbox, Communications Toolbox, DSP System Toolbox, Simscape, Simulink Support Package for Parrot Minidrones, Simulink Support Package for Raspberry Pi Hardware, and Stateflow.

---

#### 3. `img/M5-MAIN - Systems Modeling-page-28.png`
* **Slide Title:** Simulink Library Browser (MATLAB Online Editor)
* **Key Facts & Elements:**
  * **Navigation:** Highlights the **Library Browser** button located under the `Simulation` tab within the primary Simulink toolstrip.
  * **Library Browser Categories:**
    * *Standard Categories:* Commonly Used Blocks, Continuous, Dashboard, Discontinuities, Discrete, Logic and Bit Operations, Lookup Tables, Math Operations, Matrix Operations, Messages & Events, Model Verification, Model-Wide Utilities, Ports & Subsystems, Signal Attributes.
  * **Status & Environment:** Web interface (`matlab.mathworks.com`), model set to `100%` zoom, solver set to `VariableStepAuto`, default stop time `10.0` seconds.

---

#### 4. `img/M5-MAIN - Systems Modeling-page-29.png`
* **Slide Title:** Arithmetic Operations
* **Blocks Used:** `Constant`, `Add`, `Product`, `Relational Operator` (`>`), `Display`.
* **Logic Rules & Boolean Encoding:**
  * `0 = False`
  * `1 = True`
* **Formulas & Computations:**
  * **Upper Network:**
    $$\text{Sum} = (1 + 100) + (50 + 100) - 75 - 10 = 101 + 150 - 75 - 10 = 166$$
    $$\text{Multiplier} = 10 \times 1 = 10$$
    $$\text{Result} = 166 \times 10 = 1660 \quad (\text{shown in Display block})$$
  * **Lower Network (Relational Check):**
    * Compares the intermediate output $166 \times 10 = 1660$ against a constant value of $5000$:
      $$1660 > 5000 \implies \text{False} \ (0) \quad (\text{shown in Display block})$$

---

#### 5. `img/M5-MAIN - Systems Modeling-page-30.png`
* **Slide Title:** Arithmetic Operations
* **Blocks Used:** `String Constant`, `String Concat`, `String Length`, `Display`.
* **String Operations & Values:**
  * **Concatenation:**
    * String 1: `"Hello "`
    * String 2: `"FEU Tech"`
    * Operation: Concat block (`"abc"+"xyz"`)
    * Output: `'Hello FEU Tech'` (shown in Display block)
  * **Length Evaluation:**
    * Feeding concatenated string into the String Length block (`"abcdef"` icon).
    * Output Display: `16`

---

#### 6. `img/M5-MAIN - Systems Modeling-page-31.png`
* **Slide Title:** Arithmetic Operations
* **Blocks Used:** `Constant`, `Square root` ($\sqrt{u}$), `Square` ($u^2$), `Sign` (Signum), `Add`, `Relational Operator` (`==`), `Display`.
* **Formulas & Operations:**
  * **Individual Operations:**
    * $\sqrt{16} = 4$
    * $3^2 = 9$
    * $\text{sgn}(-5) = -1$
  * **Combined Equation:**
    $$\sqrt{16} + 3^2 + \text{sgn}(-5) = 4 + 9 + (-1) = 12$$
  * **Relational Comparison:**
    * Evaluates equality with `Constant3` ($12$):
      $$12 == 12 \implies \text{True} \ (1) \quad (\text{shown in Display block})$$

---

### Possible Slide Errors

1. **Slide 30 – Incorrect Slide Title:**
   * *Error:* The slide is titled **"Arithmetic Operations"**.
   * *Reason:* The slide exclusively demonstrates string manipulation (`String Constant`, `String Concat`, and `String Length`), so the title should be **"String Operations"**.

2. **Slide 30 – Unrelated Copy-Pasted Text:**
   * *Error:* The right-hand column contains the bullet points:
     * `"Greater symbol indicates the result"`
     * `"0 = False"`
     * `"1 = True"`
   * *Reason:* This text was carried over verbatim from Slide 29. Slide 30 contains no relational or comparison blocks (such as `>`), making this explanation irrelevant here.

3. **Slide 30 – Severed / Truncated Signal Wires:**
   * *Error:* The inputs feeding the lower `String Concat` block are abruptly cut off at the left edge of the cropped image.
   * *Reason:* The diagram was cropped incorrectly, leaving floating input lines without their originating source blocks.

4. **Slide 30 – Character Count Inconsistency in String Length:**
   * *Error:* The displayed string length is `16`.
   * *Reason:* The visible concatenated string `"Hello FEU Tech"` consists of 14 characters (`5` for "Hello" + `1` space + `8` for "FEU Tech"). For the length to evaluate to `16`, two hidden or extra whitespace characters must be present in the constants (e.g., `"Hello   "` or trailing spaces), which is confusing and unexplained on the slide.

5. **Slide 31 – Incomplete List of Blocks:**
   * *Error:* The list on the right only specifies `Constant`, `Square root`, `Square`, and `Sign`.
   * *Reason:* The lower diagram also uses an `Add` block, an equality `Relational Operator` (`==`), and a `Display` block, none of which are listed in the slide's block inventory.
