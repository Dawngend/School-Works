Here are the study notes for the course slides, followed by a list of identified slide errors.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-1.png`
* **Slide Title:** Modeling and Simulation
* **Key Facts:** 
  * Title/cover slide for the course.
  * Institutional affiliation: FEU Alabang, FEU Diliman, and FEU Tech.
  * Institutional slogan: "Technology Driven by Innovation".

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-2.png`
* **Slide Title:** MODULE 1: INTRODUCTION TO MODELING AND SIMULATION
* **Key Facts:** 
  * Introductory banner slide for Module 1.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-3.png`
* **Slide Title:** SUBTOPIC 1: BASIC CONCEPTS ON MODELING AND SIMULATION
* **Key Facts:** 
  * Section header establishing the fundamental principles and terminology of M&S.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-4.png`
* **Slide Title:** OBJECTIVES
* **Key Facts:** 
  * Primary goal: Demonstrate understanding of the foundational concepts of modeling and simulation.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-5.png`
* **Slide Title:** Basic Terms and Concepts: What is Modeling and Simulation (M & S)?
* **Key Facts:** 
  * M&S is a problem-centric field facilitating iterative hypothesis testing.
  * Four foundational pillars/precepts of an M&S curriculum:
    1. Modeling
    2. Simulation
    3. Visualization
    4. Analysis
  * Source: Sokolowski and Banks (2010).

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-6.png`
* **Slide Title:** Basic Terms and Concepts: What is a system?
* **Key Facts:** 
  * **INCOSE definition:** An assembly of diverse elements (people, hardware, software, facilities, policies, procedures) operating together to produce capabilities/behaviors unattainable individually.
  * **Schmidt and Taylor (1970) definition:** A collection of interacting, interdependent objects collaborating toward a shared objective.
  * An integrated framework of connected concepts or principles.
  * An aggregation of entities (parts, humans, messages, machines, servers) functioning collectively toward a goal.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-7.png`
* **Slide Title:** Basic Terms and Concepts: Types of system
* **Key Facts:** 
  * **1. Physical System:** A system that has concrete, physical existence in the real world.
  * Illustrated via an operational industrial assembly line (conveyor transporting milk cartons to a robotic packing arm).

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-8.png`
* **Slide Title:** Basic Terms and Concepts: Types of system
* **Key Facts:** 
  * **2. Notional System:** A conceptual design, proposal, or plan for a physical system that does not yet exist.
  * Illustrated via a multi-stage optical sensor and imaging pipeline:
    * `Target` (Spatially White Target) $\rightarrow$ `Atmosphere` (Turbulence & Motion Blur) $\rightarrow$ `Optics` (Diffraction, Defocus, Aberration) $\rightarrow$ `Detector` (Detector Shape) $\rightarrow$ `Processing` (Digital Filter) $\rightarrow$ `Display` (Display Filter) $\rightarrow$ `Observer` (Human Visual System).

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-9.png`
* **Slide Title:** Basic Terms and Concepts: Principal concepts in M & S – 1. System
* **Key Facts:** 
  * System definition in M&S: The core object, process, or subject under investigation and model development.
  * System classifications based on state variable transitions:
    * **a) Discrete System:** State variables change instantaneously at isolated, discrete points in time.
    * **b) Continuous System:** State variables evolve smoothly and continuously over time.
  * **State variables:** The set of variables required to fully describe the condition of a system at any instant.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-10.png`
* **Slide Title:** Basic Terms and Concepts: Principal concepts in M & S – Ways to study a system
* **Key Facts:** 
  * **Approaches to investigate a system:**
    * a) Real physical system vs. Model of the system
    * b) Physical scale model vs. Mathematical representation
    * c) Closed-form analytical solution vs. Simulation solution
  * **Modeler's core priorities:**
    * a) Performing quantitative system evaluations.
    * b) Developing methodologies for system synthesis, operational control, and optimization.
    * c) Evaluating and measuring performance metrics.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-11.png`
* **Slide Title:** Basic Terms and Concepts: Principal concepts in M & S – 2. Model
* **Key Facts:** 
  * Definition: A physical, mathematical, or logical construct representing an entity, process, or phenomenon (either historical real-world cases or synthetic use cases).
  * **Formulas & Parameters:**
    * Position: $h = \frac{1}{2}at^2 + vt + s$
    * Velocity: $v = at + v_0$
    * Constant values: $v_0 = 100\text{ ft/s}$, $s = 1000\text{ ft}$, $a = -32\text{ ft/s}^2$
  * Visual representations: 3D electromagnetic field cavity model; acoustic wavefront modulation through acoustic metafiber bundles.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-12.png`
* **Slide Title:** Basic Terms and Concepts: Principal concepts in M & S – Types of models
* **Key Facts:** 
  * **a) Physical Model:** Tangible representation (e.g., an aircraft scale model mounted in a wind tunnel).
  * **b) Notional / Abstract Model:** Conceptual, graphical, or mathematical abstraction (e.g., free-fall trajectory diagram and equation $h = \frac{1}{2}at^2 + vt + s$).

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-13.png`
* **Slide Title:** Basic Terms and Concepts: Principal concepts in M & S – 3. Simulation
* **Key Facts:** 
  * Definition: Numerical or symbolic execution replicating the dynamics and time-dependent behavior of an operational system.
  * **Simulation Code (C language):**
```c
/* Height of an object moving under gravity. */
/* Initial height v and velocity s constants. */
main()
{
    float h, v = 100.0, s = 1000.0;
    int t;
    for (t = 0, h = s; h >= 0.0; t++)
    {
        h = (-16.0 * t * t) + (v * t) + s;
        printf("Height at time %d = %f\n", t, h);
    }
}
```
  * **Slide Table Values ($t$, $v$, $h$):**
    * $t = 0$: $v = 100$, $h = 1000$
    * $t = 1$: $v = 68$, $h = 1052$
    * $t = 2$: $v = 36$, $h = 972$
    * $t = 3$: $v = 4$, $h = 860$
    * $t = 4$: $v = -28$, $h = 719$
    * $t = 5$: $v = -60$, $h = 540$
    * $t = 6$: $v = -92$, $h = 332$
    * $t = 7$: $v = -124$, $h = 92$
  * Graphic: Scatter plot of falling object height decreasing over time $t \in [0, 8]$.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-14.png`
* **Slide Title:** Basic Terms and Concepts: Principal concepts in M & S – 4. M & S
* **Key Facts:** 
  * Definition: The unified discipline combining model derivation and simulation execution to extract behavioral data for managerial, technical, and operational decision-making.
  * **Three Core Execution Steps:**
    1. Constructing a computer model representing a physical or hypothetical system.
    2. Executing the programmed model using digital computation.
    3. Analyzing, interpreting, and validating simulation results.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-15.png`
* **Slide Title:** Basic Terms and Concepts - System: Components of a System
* **Key Facts:** 
  * **System Components:**
    1. **Entity:** An object or component of specific interest within the system boundary.
    2. **Attribute:** A defining property, feature, or descriptor of an entity.
    3. **Activity:** An internal process or event driving dynamic state transitions.
  * **State of the System:** The complete instantaneous aggregate of all entities, their respective attributes, and active processes at a specific timestamp.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-16.png`
* **Slide Title:** Basic Terms and Concepts - System: Ways to Study a System
* **Key Facts:** 
  * Hierarchical taxonomy (by K. Salah):
    * `System`
      * `Experiment with the actual system`
      * `Experiment with a model of the system`
        * `Physical model`
        * `Mathematical model`
          * `Analytical solution`
          * `Simulation`

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-17.png`
* **Slide Title:** Basic Terms and Concepts - System: Examples of System
* **Key Facts:** 
  * **System Component Breakdown Table:**
    * **Supermarket:** Entity = Customers | Attribute = Shopping List | Activity = Checking-out
    * **Banking:** Entity = Customers | Attributes = Account Number, Balance, Credit Status | Activities = Deposits, Withdrawals
    * **Communication:** Entity = Messages | Attributes = Length, Priority | Activity = Transmitting
    * **Rapid Rail:** Entity = Passengers | Attributes = Origin, Destination | Activity = Traveling
    * **Traffic:** Entity = Cars | Attributes = Speed, Distance | Activity = Driving

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-18.png`
* **Slide Title:** Basic Terms and Concepts - System: System Environment & Types of Activities
* **Key Facts:** 
  * **System Environment:** External surroundings within which external influences affecting the system occur.
  * **Four Activity Classifications:**
    1. **Endogenous:** Internal activities generated within the system boundary.
    2. **Exogenous:** External activities originating in the system environment.
    3. **Deterministic:** Predictable processes where outcomes are entirely governed by known inputs.
    4. **Stochastic:** Probabilistic processes involving random variables where outputs cannot be deterministically computed solely from inputs.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-19.png`
* **Slide Title:** Basic Terms and Concepts - System: Examples: Endogenous and Exogenous Activity
* **Key Facts:** 
  * **Activity Examples Table:**
    * **Supermarket:** Endogenous = Purchasing, Check-out | Exogenous = Arrival of Customers in Supermarket
    * **Car Parking in Supermarket:** Endogenous = Arrival of Customers in Supermarket | Exogenous = Arrival of Cars

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-20.png`
* **Slide Title:** Basic Terms and Concepts - System: Types of System
* **Key Facts:** 
  * **System Categories:**
    1. **Open:** Interacts with its environment via exogenous activities.
    2. **Closed:** Self-contained system isolated from exogenous activities.
    3. **Continuous:** Experiences gradual, continuously smooth state changes (e.g., flight dynamics of an aircraft).
    4. **Discrete:** Experiences state changes at distinct, discontinuous epochs (e.g., a factory production floor).
    5. **Sampled-data:** System governed by continuous dynamics, but sampled or measured only at discrete time intervals.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-21.png`
* **Slide Title:** Basic Terms and Concepts - System: Why model a system?
* **Key Facts:** 
  * Four primary justifications for simulation over direct system experimentation:
    1. Physical system is inaccessible (e.g., deep space, microscopic scale).
    2. Direct experimentation poses severe danger (e.g., nuclear accidents, crash testing).
    3. Physical trials are ethically, economically, or operationally unacceptable (e.g., intentionally failing hospital logistics).
    4. The system is non-existent / purely conceptual.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-22.png`
* **Slide Title:** Basic Terms and Concepts - Model: Subtasks in Deriving a Model
* **Key Facts:** 
  * **1. Establishing Model Structure:**
    * a. Delineating system boundaries.
    * b. Identifying constituent entities, attributes, and activities.
  * **2. Supplying Data:**
    * a. Specifying numeric and qualitative values for attributes.
    * b. Formulating functional relationships governing activities.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-23.png`
* **Slide Title:** Basic Terms and Concepts - Model: Types of Models
* **Key Facts:** 
  * **Classification Tree:**
    * `Models`
      * `Physical`: Divided into `Static` and `Dynamic`.
      * `Mathematical`: Divided into:
        * `Static`: Solved via `Numerical Technique` or `Analytical Technique`.
        * `Dynamic`: Solved via `Analytical Technique` or `Numerical Technique` (leading directly to `System simulation`).

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-24.png`
* **Slide Title:** Basic Terms and Concepts - Modelling: Definition of Modeling (Modelling)
* **Key Facts:** 
  * Modeling encompasses model specification, construction, and operational definition.
  * Synthesizes an abstract representation capturing essential properties of a target system.
  * Enables analysts to forecast responses to system modifications without altering the physical system.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-25.png`
* **Slide Title:** Basic Terms and Concepts - Modelling: Principles used in Modeling
* **Key Facts:** 
  * **1. Block Building:** Decomposing complex systems into modular blocks with defined inputs and outputs connected to form an overall block diagram.
  * **2. Relevance:** Restricting model contents strictly to aspects pertinent to the study's scope and objectives.
  * **3. Accuracy:** Ensuring empirical data and structural formulations are correct and valid.
  * **4. Aggregation:** Combining smaller individual entities into higher-level aggregated groups to balance fidelity against computational complexity.

---

### Possible Slide Errors

1. **Slide 6 — Typo / Grammar Error:**
   * *Error:* "...behavior an performance."
   * *Correction:* The conjunction "and" is misspelled as "an".

2. **Slide 7 — Subject-Verb Agreement:**
   * *Error:* "Something that already exist"
   * *Correction:* "Something" is singular, so the verb should be "exists".

3. **Slide 11 — Formula Typo / Jammed Text:**
   * *Error:* The equation box displays `Model: h = 1/2 at^2 + vt + sv = at + v_0`.
   * *Correction:* The position equation ($h = \frac{1}{2}at^2 + v_0t + s_0$) and the velocity equation ($v = at + v_0$) are run together without spacing or punctuation, creating the erroneous combined expression `+ sv = at + v_0`. Furthermore, the linear velocity term in the position equation should use initial velocity $v_0$ rather than instantaneous $v$.

4. **Slide 11 — Grammatical Agreement:**
   * *Error:* "It serves as representations of events and/or things..."
   * *Correction:* Mixed singular subject and plural predicate nominative; it should read "It serves as a representation..." or "Models serve as representations...".

5. **Slide 13 — Code Comment Inversion:**
   * *Error:* The comment states: `/* Initial height v and velocity s constants. */`
   * *Correction:* In physics and in the code line directly below (`float h, v = 100.0, s = 1000.0;`), $v$ represents initial velocity ($100\text{ ft/s}$) and $s$ represents initial height/position ($1000\text{ ft}$). The comment reverses these variable definitions.

6. **Slide 13 — Discrepancy Between Code and Slide Table / Physics Calculations:**
   * *Error:* The table lists $t=1 \implies h=1052$ and $t=2 \implies h=972$.
   * *Correction:* Evaluating the equation given in the code ($h = -16t^2 + 100t + 1000$):
     * For $t=1$: $h = -16(1) + 100 + 1000 = 1084$ (not $1052$).
     * For $t=2$: $h = -16(4) + 200 + 1000 = 1136$ (not $972$).
     * The table values in the slide do not match the parabolic equation computed by the code.

7. **Slide 13 — Loop Logic / Termination Bug in C Code:**
   * *Error:* The loop condition `for (t = 0, h = s; h >= 0.0; t++)` evaluates `h` computed from the *previous* iteration before recalculating `h` inside the body.
   * *Correction:* When $h$ becomes negative, the loop executes one additional time, printing a negative height before the loop condition fails.

8. **Slide 14 — Grammatical Tense Error:**
   * *Error:* "It used models and simulations to develop data..."
   * *Correction:* Should be in the present tense: "It uses models and simulations...".

9. **Slide 18 — Redundant / Confusing Phrasing in Stochastic Definition:**
   * *Error:* "Activities wherein the outputs cannot be described in terms of its input or outputs"
   * *Correction:* Saying outputs cannot be described in terms of "outputs" is circular; it should state that outputs cannot be deterministically predicted solely from inputs due to inherent random variation.

10. **Slide 19 — Questionable Classification in Example Table:**
    * *Error:* For the system "Car Parking in Supermarket", "Arrival of Customers in Supermarket" is categorized as *Endogenous*, while "Arrival of Cars" is categorized as *Exogenous*.
    * *Correction:* For a car parking lot system, cars arriving are the primary entities entering the boundary, while customers entering the physical supermarket happen downstream or outside the parking lot boundary, making this pairing inverted or poorly scoped.

11. **Slide 20 — Subject-Verb Agreement:**
    * *Error:* "A system which don't have any exogenous activities."
    * *Correction:* "System" is singular; it should be "doesn't have" (or "does not have").

12. **Slide 24 — Incomplete Sentence / Truncated Text:**
    * *Error:* The final sentence cuts off mid-thought: "In other words, modelling"
    * *Correction:* The sentence is truncated at the end of the slide without a period or closing thought.

13. **Slide 25 — Spelling and Grammatical Errors:**
    * *Errors:*
      * Under Block Building: "Each block describe a part of the system." (Should be "describes").
      * Under Relevance: "...only include relevant aspect of the system." (Should be "aspects").
      * Under Aggregation: "It is the extend to which..." (Should be the noun "extent", not the verb "extend").

### Slide Study Notes

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-26.png`
- **Slide Title**: Basic Terms and Concepts - Simulation: What is Simulation?
- **Key Concepts & Facts**:
  - **Simulation Definition**: The process of mimicking the behavior of a system, facility, or operational process over time or space, predominantly using computer-based environments.
  - **System**: The actual entity or process targeted for study.
  - **Model**: An aggregated collection of logical and mathematical assumptions/approximations representing system structure and operation.
  - **Analytical Solution**: An exact, closed-form mathematical solution achievable only when the model's formulation is sufficiently simple.
  - Simulation serves to evaluate the operational performance of both existing systems and proposed designs.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-27.png`
- **Slide Title**: Basic Terms and Concepts - Simulation: History of Simulation
- **Key Dates & Milestones**:
  - **1940**: Development of the Monte Carlo method by researchers (John von Neumann, Stanislaw Ulam, Edward Teller, Herman Kahn) alongside Manhattan Project physicists investigating neutron scattering.
  - **1960**: Emergence of specialized simulation programming languages, notably SIMSCRIPT developed by Harry Markowitz at the RAND Corporation.
  - **1970**: Formal establishment and academic study of the mathematical foundations of simulation.
  - **1980**: Proliferation of PC-compatible simulation tools, interactive graphical user interfaces (GUIs), and object-oriented programming (OOP).
  - **1990**: Rise of web-based simulation tools, high-fidelity animated graphics, simulation-based optimization methods, and Markov-chain Monte Carlo (MCMC) algorithms.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-28.png`
- **Slide Title**: Basic Terms and Concepts - Simulation: Some (not all) application areas for simulation
- **Key Fields & Applications**:
  - Manufacturing line optimization, layout design, and throughput analysis.
  - Military defense evaluations, weapon capability assessments, and logistical support.
  - Communication network protocol validation and hardware infrastructure requirements.
  - Computer system hardware/software architecture sizing.
  - Large-scale transport logistics (airports, highway traffic, maritime ports, rapid transit).
  - Service sector operations (call centers, hospitals, postal facilities, quick-service dining).
  - Business Process Reengineering (BPR).
  - Supply chain stock sizing and inventory replenishment policies.
  - Financial, econometric, and market trend forecasting.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-29.png`
- **Slide Title**: Basic Terms and Concepts - Simulation: The Process of Simulation
- **Workflow / Process Steps**:
  1. Define Problem
  2. Introduce Important Variables
  3. Construct Simulation Model
  4. Specify Values of Variables to Be Tested
  5. Conduct the Simulation
  6. Examine the Results
  7. Select Best Course of Action
  - *Feedback Loops*: Examination of results can trigger iterations back to refining the model construction or adjusting variable test values.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-30.png`
- **Slide Title**: Basic Terms and Concepts - Simulation: Classification of Simulation Models
- **Key Categories**:
  - Static vs. Dynamic
  - Deterministic vs. Stochastic
  - Continuous vs. Discrete
  - *Core Insight*: Most real-world operational models combine dynamic, stochastic, and discrete properties, generally designated as **discrete-event simulation (DES)** models.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-31.png`
- **Slide Title**: Basic Terms and Concepts - Simulation: Other Types of Simulation
- **Key Types Listed**:
  1. Hybrid Simulation
  2. Real-time Simulation
  3. Web-based Simulation

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-32.png`
- **Slide Title**: Basic Terms and Concepts – System Simulation: System Simulation
- **Core Definition & Method Comparison**:
  - **System Simulation**: Problem-solving technique evaluating a system by observing the temporal behavior of its dynamic model.
  - **Analytical Method**:
    - Best suited for straightforward, highly tractable models.
    - Uses exact mathematical mechanisms (calculus, algebra, probability theory) to calculate closed-form solutions.
  - **Simulation Method**:
    - Employed when system dynamics are too intricate for exact analytical treatment.
    - Utilizes numerical computation on computers to generate data points and empirically estimate system properties.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-33.png`
- **Slide Title**: Basic Terms and Concepts – System Simulation: Analytical Method vs. Simulation Method
- **Key Points Comparison**:
  - *Scope*: Analytical produces general solutions covering all conditions; simulation produces specific solutions for specifically configured test runs.
  - *Applicability*: Analytical is restricted to simpler mathematical formulations; simulation extends mathematical feasibility to arbitrary complexity.
  - *Computational Output*: Analytical solutions may yield intractable integrals or series requiring intensive numerical evaluation; simulation offers a direct, fast numerical approximation.
  - *Constraints & Delays*: Analytical models struggle with non-linear forces, dead stops, or step delays; simulation handles physical stops and non-linearities naturally.
  - *Logic Type*: Analytical relies on deductive mathematical logic; simulation utilizes numerical and computational execution.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-34.png`
- **Slide Title**: Basic Terms and Concepts – M & S: Advantages of Modeling and Simulation
- **Key Benefits**:
  - **Easy to understand**: Visualizes and explains system interactions safely without interfering with active real-world operations.
  - **Easy to test**: Safely test parameter adjustments and observe downstream output effects risk-free.
  - **Easy to upgrade**: Determines capacity, equipment, or architectural requirements under alternative operating configurations.
  - **Easy to identify constraints**: Locates operational and informational bottlenecks producing lag.
  - **Easy to diagnose problems**: Untangles complex multi-variable interactions and tests revised operating policies safely.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-35.png`
- **Slide Title**: Basic Terms and Concepts – M & S: Disadvantages of Modeling and Simulation
- **Key Drawbacks**:
  - Building effective models is an art requiring high domain expertise, training, and experience.
  - Reliance on pseudo-random numbers introduces stochastic variation, requiring multiple runs and careful output interpretation.
  - Development is often labor-intensive, time-consuming, and computationally/financially expensive.
  - Simulation output datasets can be difficult to interpret, often necessitating specialized statistical knowledge.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-36.png`
- **Slide Title**: Basic Terms and Concepts – M & S: Steps in Simulation and Model Building
- **10 Sequential Steps**:
  1. Define an achievable goal
  2. Put together a complete mix of skills on the team
  3. Involve the end-user
  4. Choose the appropriate simulation tools
  5. Model the appropriate level(s) of detail
  6. Start early to collect the necessary input data
  7. Provide adequate and on-going documentation
  8. Develop a plan for adequate model verification (*"Did we get the 'right answers?'"*)
  9. Develop a plan for model validation (*"Did we ask the 'right questions?'"*)
  10. Develop a plan for statistical output analysis

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-37.png`
- **Slide Title**: M & S Development Process Cycle: M & S Development Process Cycle & Relevant Technologies
- **Cyclic Flow**:
  - `Model` $\xrightarrow{\text{Implement}}$ `Simulation` $\xrightarrow{\text{Execute}}$ `Results` $\xrightarrow{\text{Analyze}}$ `Insight` $\xrightarrow{\text{Model}}$ `Model`
- **Technology Quadrants**:
  - **Modeling technologies** (Top-Left): Underpin model creation via algorithms, paradigms, and mathematical theories.
  - **Development technologies** (Top-Right): Software engineering tools and project management for building the simulation code.
  - **Computation technologies** (Bottom-Right): Hardware host architectures and computing platforms that run executions.
  - **Data/information technologies** (Bottom-Left): Capture, transformation, statistical analysis, and VV&A (Verification, Validation, and Accreditation).

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-38.png`
- **Slide Title**: M & S Development Process Cycle: Phases of a Cyclic Movement of Process of M&S
- **Phase-to-Technology Mapping**:
  1. `Model Phase` = modeling technologies
  2. `Code Phase` = development technologies
  3. `Execute Phase` = computational technologies
  4. `Analyze Phase` = data/information technologies

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-39.png`
- **Slide Title**: Related Disciplines: 1. Probability and Statistics
- **Key Concepts & Examples**:
  - Generates random variates to capture input uncertainty/variability and interprets output data from stochastic models.
  - *Stoplight Uncertainty Example*:
    - Time delay before the lead driver perceives a green light.
    - Take-off acceleration of the lead vehicle.
    - Reaction time before the trailing vehicle moves.
    - Inter-vehicle headway/spatial distance.
    - System delay propagated if a vehicle stalls.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-40.png`
- **Slide Title**: Related Disciplines: 2. Analysis and Operations Research
- **Key Definitions**:
  - **Data Context**: Simulations output voluminous datasets preserved as multi-dimensional arrays.
  - **Analysis**: Converting raw numerical arrays into descriptive operational insight.
  - **Operations Research**: Designing and deploying analytical and optimization techniques to extract meaning from the data.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-41.png`
- **Slide Title**: Related Disciplines: 3. Computer Visualization, 4. Human Factors, 5. Project Management
- **Key Concepts**:
  - **Computer Visualization**:
    - *Visualization*: Visual data interfaces enabling intuitive interpretation of model states.
    - *Animations*: Dynamic graphical displays portraying temporal evolution.
  - **Human Factors**: Applying knowledge of human perception and cognition to simulation interface design.
  - **Project Management**: Governing schedule, budget, and cross-functional teams when simulation serves as the primary investigative technique for large-scale systems.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-42.png`
- **Slide Title**: Characteristics and Descriptors – Simulation Paradigms: 1. Monte Carlo Simulation
- **Key Concepts & Graphic**:
  - Samples repeatedly from known input probability distributions to generate output distributions.
  - Evaluates system variability through repeated random sampling.
  - *Figure*: "100000 Monte Carlo Simulations Based On Taking Random Samples", showing projected market capitalization trajectories from mid-2018 to early 2019 relative to a baseline threshold of $5 \times 10^{11}$ USD.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-43.png`
- **Slide Title**: Characteristics and Descriptors – Simulation Paradigms: 2. Continuous Simulation
- **Key Concepts & Formulas**:
  - System state variables change continuously as smooth functions over time.
  - Formulated mathematically using differential equations.
  - *Transistor RC Charging Formula*:
    $$V_t = V_{\text{DD}}(1 - e^{-t/(RC_L)})$$
  - Graph illustrates voltage $V_t$ asymptotically approaching source supply $V_{\text{DD}}$ across continuous time $t$.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-44.png`
- **Slide Title**: Characteristics and Descriptors – Simulation Paradigms: 3. Discrete-Event Simulation
- **Key Concepts & Diagram**:
  - State variables change instantaneously only at discrete points in time when specific events occur.
  - Simulation clock jumps forward from the timestamp of one event directly to the next.
  - Closely tied to queuing network models.
  - *Emergency Department Process Model*:
    - Patient arrival (A) $\rightarrow$ Triage acuity check (B) $\rightarrow$ Waiting room (C) $\rightarrow$ Treatment area exam (D) $\rightarrow$ Disposition decision (E): outpatient discharge or in-patient bed wait (F) leading to admission; includes balking branch ("Leave without being seen").

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-45.png`
- **Slide Title**: Characteristics and Descriptors – M & S Attributes: 1. Fidelity
- **Key Definitions**:
  - **Fidelity**: How accurately a model or simulation reflects real-world physics, behavior, and environment.
  - **High Fidelity**: Very close adherence to real-world behavior; difficult and costly to achieve.
  - **Low Fidelity**: Coarse approximation acceptable for system elements non-essential to the primary research questions.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-46.png`
- **Slide Title**: Characteristics and Descriptors – M & S Attributes: 2. Resolution, 3. Scale
- **Key Definitions**:
  - **Resolution (Granularity)**: The depth or granularity of detail embedded in the model.
    - *High Resolution*: Highly detailed representation of individual components or subsystems.
  - **Scale (Level)**: The aggregate physical size, operational tier, or operational boundary spanned by the scenario.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-47.png`
- **Slide Title**: Characteristics and Descriptors – M & S Attributes: Tables 1.1, 1.2, 1.3
- **Table Values**:
  - **Table 1.1: Comparing fidelity and resolution**
    - Low Resolution, Low Fidelity: *Board game—chess*
    - Low Resolution, High Fidelity: *Agent-based simulation—Swarm*
    - High Resolution, Low Fidelity: *Personal computer flight simulator—Microsoft Flight Simulator*
    - High Resolution, High Fidelity: *Platform-level training simulation—airline flight simulator*
  - **Table 1.2: Comparing fidelity and scale**
    - High Scale, Low Fidelity: *Board game—Battleground*
    - High Scale, High Fidelity: *Massive multiplayer online games—World of Warcraft*
    - Low Scale, Low Fidelity: *Personal computer combat simulator—Doom*
    - Low Scale, High Fidelity: *First-person shooter—Halo*
  - **Table 1.3: Comparing resolution and scale**
    - Low Scale, Low Resolution: *Not interesting*
    - Low Scale, High Resolution: *Urban warfare personal computer game—Shrapnel: Urban Warfare 2025*
    - High Scale, Low Resolution: *Operational-level training simulation—WarSim*
    - High Scale, High Resolution: *Not practical*

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-48.png`
- **Slide Title**: Characteristics and Descriptors – Model Types: 1. Physics-Based Modeling, 2. Finite Element Modeling (FEM)
- **Key Descriptions & Examples**:
  - **Physics-Based Modeling**:
    - Governed by mathematical relations derived directly from first physical principles (e.g., conservation laws).
    - *Example*: Newton’s law of universal gravitation.
  - **Finite Element Modeling (FEM)**:
    - Analyzes complex continuous bodies by subdividing them into meshes of simpler, discrete geometric sub-elements.
    - *Application*: Structural mechanics, stress analysis, and aerodynamics in aerospace engineering.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-49.png`
- **Slide Title**: Characteristics and Descriptors – Model Types: 3. Data-Based Modeling, 4. Agent-Based Modeling (ABM), 5. Aggregate Modeling
- **Key Definitions**:
  - **Data-Based Modeling**: Derived empirically from observed datasets describing system states; ideal when internal physical mechanisms are inaccessible or notional.
  - **Agent-Based Modeling (ABM)**: Simulates decentralized autonomous entities (agents) to examine emergent macro-level social, economic, or biological phenomena.
  - **Aggregate Modeling**: Bundles multiple low-level entities or micro-actions into combined macro entities to simplify constructive models.

---

#### `img/M1-MAIN-Introduction to Modeling and Simulation-page-50.png`
- **Slide Title**: Characteristics and Descriptors – Model Types: 6. Hybrid Modeling, Note: Other model types
- **Key Models**:
  - **Hybrid Modeling**: Combines multiple modeling paradigms (e.g., continuous + discrete event) within a single architecture.
  - **Additional Paradigms**:
    - Markov Chains
    - Finite-state Automata
    - Particle Systems
    - Queuing Models
    - Bond Graphs
    - Petri Nets

---

### Possible slide errors

1. **Slide 27 — Typo in Mathematician's Name**:
   - The slide spells Stanislaw Ulam's name as **"Stanislaw Ulan"**. The co-inventor of the Monte Carlo method is *Stanislaw Ulam* (ending in 'm').

2. **Slide 33 — Grammar and Generalization Errors**:
   - Point 3 under Analytical Method states: *"There is limited problem that can be solved mathematically."* This contains a grammatical error and should read *"There are limited problems..."* or *"Only a limited set of problems can be solved mathematically."*
   - Point 5 under Simulation Method asserts: *"Gives results in few minutes at a very low cost."* Aside from missing the article (*"in a few minutes"*), this is an overgeneralization; large-scale complex simulations often require days of high-performance computing clusters and substantial engineering costs.

3. **Slide 34 — Grammatical Inconsistency**:
   - Bullet 4 heading reads **"Easy to identifying constraints"**, which violates parallel grammatical structure with the other bullet headers (*"Easy to understand"*, *"Easy to test"*, *"Easy to upgrade"*). It should read **"Easy to identify constraints"**.

4. **Slide 36 — Inverted / Non-Standard Verification vs. Validation Definitions**:
   - Step 8 defines verification as *(Did we get the “right answers?”)* and Step 9 defines validation as *(Did we ask the “right questions?”)*.
   - In standard systems engineering and M&S literature (e.g., IEEE, DoD, and Balci's classic guidelines):
     - **Verification** addresses: *"Did we build the system/model right?"* (checking that the implementation matches specifications and contains no bugs).
     - **Validation** addresses: *"Did we build the right system/model?"* (checking that the model accurately reflects real-world physics/requirements).

5. **Slide 43 — Inaccurate Physical Model Equation**:
   - The caption states the graph represents a *"depletion mode transistor acting as a pull up for a capacitive load"*, but the formula given is $V_t = V_{\text{DD}}(1 - e^{-t/(RC_L)})$. This formula describes an ideal linear resistor charging a capacitor. A depletion-mode MOSFET pull-up exhibits a nonlinear current-voltage characteristic ($I_{\text{DS}}$ varies nonlinearly with $V_{\text{DS}}$), which produces a distinct charging profile rather than a simple single-time-constant linear RC exponential curve.

6. **Slide 48 — Tense Inconsistency**:
   - Under Physics-Based Modeling, the bullet reads: *"Method of modeling that used mathematical models where..."* It should use the present tense **"uses"** rather than the past tense **"used"**.

### Study Notes by Slide

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-51.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-51.png)
- **Title**: M & S Category Dimensions : Type (Classifications)
- **Notes**:
  - Focuses on **Live Simulation**: real people operating real systems/equipment.
  - Highlights the *CyberSurgeons* live simulation program at Worcester Preparatory School, where 10th-grade AP Biology students acted as medical personnel diagnosing and treating simulated ailments along a virtual Amazon River expedition.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-52.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-52.png)
- **Title**: M & S Category Dimensions : Type (Classifications)
- **Notes**:
  - Focuses on **Virtual Simulation**: real human participants operating inside synthetic, simulated systems.
  - Environment is engineered to recreate realistic operational conditions.
  - Example shown: cockpit flight training using the `CNFSimulator.FTD.A320 Flight Simulator`.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-53.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-53.png)
- **Title**: M & S Category Dimensions : Type (Classifications)
- **Notes**:
  - Focuses on **Constructive Simulation**: real humans supply inputs/parameters, while simulated actors operate simulated systems to execute those behaviors.
  - Example shown: US Military's Modular Semi-Automated Forces (**ModSAF**), utilized for doctrine evaluation and tactical rules of engagement training.
  - Visuals show the ModSAF map grid interface and simulated helicopter unit positions.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-54.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-54.png)
- **Title**: M & S Category Dimensions : Type (Classifications)
- **Notes**:
  - Summarizes the participant-to-system relationship across simulation types:
  - **Table 1.4: M&S types**
    | Category | Participants | Systems |
    | :--- | :--- | :--- |
    | Live | Real | Real |
    | Virtual | Real | Simulated |
    | Constructive | Simulated | Simulated |

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-55.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-55.png)
- **Title**: M & S Category Dimensions : Applications
- **Notes**:
  - Defines applications as the core objectives behind creating M&S solutions.
  - **1. Training Applications**: Aimed at knowledge acquisition and performance skill development for users.
  - **2. Analysis Applications**: Detailed investigation of a system to evaluate design alternatives, predict behavior, and test performance across scenarios.
  - **3. Experimentation Applications**: Iterative testing to navigate design solution spaces, clarify ambiguous system dynamics, and discover high-value interventions.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-56.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-56.png)
- **Title**: M & S Category Dimensions : Applications
- **Notes**:
  - **4. Engineering Applications**: System design and validation via simulated testbeds where model validity is the prime objective. Tools highlighted: Finite Element analysis packages, MATLAB (continuous-time systems), and ARENA (discrete-event systems).
  - **5. Acquisition Applications**: Guides decision-making throughout the whole product life cycle (from inception to disposal) to verify system efficacy and financial viability before committing acquisition funds.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-57.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-57.png)
- **Title**: M & S Category Dimensions : Randomness
- **Notes**:
  - Evaluates whether stochastic behavior and uncertainty exist within the model.
  - **Deterministic Simulation**: A fixed set of inputs strictly produces a unique, repeatable set of outputs without uncertainty (e.g., classical physics-based models, deterministic engineering models).
  - **Stochastic Simulation**: Driven by random input variables producing random output distributions; requires rigorous inferential statistical tools (e.g., discrete-event queuing models).

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-58.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-58.png)
- **Title**: M & S Category Dimensions : Domain
- **Notes**:
  - Identifies the domain as the specific operational discipline or subject field of the M&S process.
  - Examples: Military, Transportation, Decision Support, Game-based Learning, and Healthcare/Medical simulations.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-59.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-59.png)
- **Title**: Formative Assessment 1
- **Notes**:
  - Administrative checkpoint directing students to Canvas for instructions on Formative Assessment 1.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-60.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-60.png)
- **Title**: Summative Assessment 1
- **Notes**:
  - Administrative checkpoint directing students to Canvas for instructions on Summative Assessment 1.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-61.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-61.png)
- **Title**: References
- **Notes**:
  - Online source: `www.tutorialspoint.com`
  - Textbooks cited:
    - Sokolowski, J. A. & Banks, C. M. (2010). *Modeling and Simulation Fundamentals Theoretical Underpinnings and Practical Domains*. John Wiley & Sons.
    - Singh, P. & Singh, N. (2012). *Modeling and Simulation*. S K Kataria and Sons.
    - Schmidt and Taylor. (1970). *Modeling and Analysis*.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-62.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-62.png)
- **Title**: Introduction to MATLAB (Modeling and Simulation)
- **Notes**:
  - Unit division slide introducing the MATLAB portion of the course module.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-63.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-63.png)
- **Title**: Subtopic 2 MATLAB Programming: Modeling and Simulation in MATLAB
- **Notes**:
  - Topic header slide establishing Subtopic 2: Modeling and Simulation within MATLAB.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-64.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-64.png)
- **Title**: OBJECTIVES
- **Notes**:
  - Define Modeling and Simulation.
  - Explain MATLAB and its functions.
  - Understand fundamental MATLAB concepts and syntax.
  - Identify built-in functions used in interactive evaluations.
  - Master vector and matrix representations and operations.
  - Apply built-in routines to optimize vector and matrix computations.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-65.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-65.png)
- **Title**: What is Modeling
- **Notes**:
  - Defines modeling as:
    - The specific act or procedure of constructing a model.
    - The professional practice or occupation of modeling physical or abstract systems.
  - Includes a visual of an engineer analyzing finite-element and thermal CAD models across workstations.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-66.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-66.png)
- **Title**: What is Simulation
- **Notes**:
  - Characterizes a simulation model as a mathematical framework measuring how uncertain inputs and user decisions affect business or system outcomes (e.g., profit/loss, ROI).
  - Core components:
    - Uncertain model inputs (random input variables).
    - Required intermediate computational steps.
    - Model outputs that depend on inputs (uncertain outcome functions).

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-67.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-67.png)
- **Title**: What is Simulation
- **Notes**:
  - General definition: The imitation of an actual real-world object, system, or operational process.
  - Involves abstracting key operational properties and behaviors into a model.
  - Defined as designing an artificial system model and running experiments to observe and understand operational behavior.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-68.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-68.png)
- **Title**: Simulation techniques
- **Notes**:
  - Deployed for managerial decision-making whenever exact analytical or closed-form solutions are absent or computationally intractable.
  - Typical operational areas:
    - Inventory control
    - Queuing systems
    - Production and scheduling planning

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-69.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-69.png)
- **Title**: Simulation Application Sample
- **Notes**:
  - Explores **AnyLogic**: highlights its integrated GIS mapping engine to track geospatial routing, supply networks, and regional transportation links.
  - Relevant industry domains highlighted: Supply Chains, Transportation, Rail Logistics, Oil & Gas, Manufacturing, Warehouse Operations, Mining, and Ports & Terminals.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-70.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-70.png)
- **Title**: Simulation Application Sample
- **Notes**:
  - Highlights **GeoFS**: browser-based flight simulator rendering global terrain via satellite photography and digital elevation data (supporting mobile and VFR navigation).
  - Highlights **Morild Interaktiv** (`https://www.morildinteraktiv.no/custom`): commercial provider of immersive VR maritime training simulators.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-71.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-71.png)
- **Title**: Simulation Application Sample
- **Notes**:
  - Displays a list labeled "10+ Network Simulation Tools & Softwares":
    - GNS3 (Graphical Network System 3), Cisco Packet Tracer, PuTTY, Secure CRT, Microsoft Visio, PRTG Network Monitor, WIRESHARK, EVE-NG, Network Simulator - NS3, and SNMP Agent Simulator.
  - Visual illustrates a 3-tier hierarchical enterprise network topology modeled inside Cisco Packet Tracer.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-72.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-72.png)
- **Title**: Subtopic 2 MATLAB Programming: Introduction to MATLAB
- **Notes**:
  - Dedicated subtopic transition slide for the introductory overview of MATLAB.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-73.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-73.png)
- **Title**: What is MATLAB
- **Notes**:
  - Definition: High-performance software environment specialized for numeric calculation, algorithm development, data visualization, and matrix programming.
  - Origin: Name derives from **Matrix Laboratory**. Created originally to provide easy access to matrix software developed by the **LINPACK** (*Linear system package*) and **EISPACK** (*Eigen system package*) projects.
  - Features: Native matrix manipulation language, built-in editor/debugger, advanced data structures, and object-oriented programming.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-74.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-74.png)
- **Title**: What is MATLAB
- **Notes**:
  - Highlights MATLAB's multi-paradigm capability: supporting Functional, Object-Oriented, and Visual programming models.
  - Supports rapid enterprise scaling and embedded system targets, connecting with Simulink® and Model-Based Design workflows.
  - Shows an embedded C code snippet illustrating bit-field structure sizing:
    ```c
    struct TCS {
        int x: 1;
        int y: 2;
        int z: 4;
        int w: 8;
    } A;

    int main() {
        printf("%d", sizeof(A));
        return 0;
    }
    ```

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-75.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-75.png)
- **Title**: What is MATLAB
- **Notes**:
  - Core functional capabilities:
    1. Matrix manipulation
    2. Algorithm implementation
    3. Data and function plotting
    4. Inter-language interoperability
  - Displays external language bridges supported by MATLAB: C, C++, Java, Python, and .NET.

---

### Possible slide errors

1. **Slide 57 — Grammatical agreement error**:
   - The bullet points state: *"This simulation include no uncertainty..."* and *"This simulation include uncertainty..."*
   - *Reason*: "Simulation" is singular and requires the singular verb form "includes".

2. **Slide 64 — Punctuation and typographical errors in objectives**:
   - Bullet 2 reads: *"Know what is Matlab and it’s function"*.
   - *Reason*: "It's" is a contraction for "it is"; the possessive adjective is "its". Additionally, "Matlab" uses title case here while bullets 3 and 4 capitalize it as "MATLAB".
   - Bullet 7 reads: *"Use build-in functions to simplify codes..."*.
   - *Reason*: The adjective is "built-in", not "build-in".

3. **Slide 65 — Subject-verb agreement error**:
   - Bullet 2 reads: *"the practice or occupation of a person who model objects"*.
   - *Reason*: The singular relative pronoun antecedent "person" requires the singular verb "models", not "model".

4. **Slide 67 — Tense and grammatical infinitive errors**:
   - Bullet 2 states: *"The act of simulating something generally involved representation..."*.
   - *Reason*: Uses past tense ("involved") in a general present-tense definition (should be "involves").
   - Bullet 3 states: *"...for the purpose of understand the behavior..."*.
   - *Reason*: Following the preposition "of", the gerund form "understanding" is required.
   - There is also an isolated dangling period on a line by itself at the bottom of the text block.

5. **Slide 71 — Inaccurate tool categorization and terminology**:
   - The slide is titled *"List of 10+ Network Simulation Tools & Softwares"*.
   - *Reason*: Several listed items are **not** network simulation software:
     - **PuTTY** and **SecureCRT** are SSH/Telnet terminal clients, not network simulators.
     - **Wireshark** is a packet sniffer and protocol analyzer for live or captured traffic, not a simulation tool.
     - **Microsoft Visio** is a general diagramming and vector drawing application.
     - **PRTG Network Monitor** is a live network infrastructure monitoring platform.
     - Additionally, "Softwares" is non-standard English ("software" is an uncountable mass noun).

6. **Slide 74 — Irrelevant code snippet image**:
   - The slide discusses MATLAB's multi-paradigm programming and Simulink integration, but features a screenshot titled *"Programming with C"* containing a multiple-choice question on C bit-field memory sizing (`struct TCS { int x: 1; ... }`).
   - *Reason*: This C language low-level memory allocation snippet has no pedagogical connection to MATLAB's high-level multi-paradigm or Model-Based Design capabilities.

### Slide Study Notes

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-76.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-76.png)
- **Slide Title**: Subtopic 2: MATLAB Programming: Basics of MATLAB
- **Key Facts**:
  - Title/divider slide introducing Subtopic 2: fundamental concepts and environment basics of MATLAB programming.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-77.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-77.png)
- **Slide Title**: Subtopic 2: BASICS OF MATLAB
- **Key Facts**:
  - Secondary title banner marking the start of the MATLAB basics lecture.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-78.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-78.png)
- **Slide Title**: OBJECTIVES
- **Key Facts & Objectives**:
  - Understand fundamental MATLAB concepts and environment tools.
  - Identify and use built-in functions inside interactive expressions.
  - Understand concepts, representations, and operations on vectors and matrices.
  - Apply built-in functions to streamline and simplify matrix/vector code.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-79.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-79.png)
- **Slide Title**: Basics of MATLAB – Local Environment
- **Key Facts & Numbers**:
  - **Access routes**: IT administrator remote access, or local installation.
  - **Installation specs**: Trial version download size $\approx 5\text{ GB}$; installation duration $\approx 20\text{ minutes}$.
  - **URL**: `https://www.mathworks.com/downloads/web_downloads/`

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-80.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-80.png)
- **Slide Title**: Basics of MATLAB – GUI Layout (MATLAB R2012b)
- **Key Windows & Interface Elements**:
  - **Current Folder Window**: Shows the active directory and saved scripts/data files (e.g., `experd.dat`, `calcarea.m`, `circlescript.m`).
  - **Command Window**: Prompt (`>>` / `fx >>`) for interactive command entry.
  - **Workspace Window**: Displays currently defined and imported variables with values/dimensions (e.g., `num: 8`, `res: 7`, `x`, `y`).
  - **Command History Window**: Logs previously executed statements (e.g., `res = 9 - 2;`, `num = res;`, `x = 1:4;`).

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-81.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-81.png)
- **Slide Title**: Basics of MATLAB – Interactive Commands
- **Key Commands**:
  - `demo`: Launches MATLAB interactive demos and examples in the Help Browser.
  - `help`: Explains any function directly in the Command Window; `help help` explains the help system itself.
  - `lookfor`: Keyword search through all help entries (can take longer to run).
  - `doc`: Opens the official documentation page in the Help Browser.
  - **Exiting**: Enter `quit` or `exit` at the prompt, or select menu item `MATLAB > Quit MATLAB`.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-82.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-82.png)
- **Slide Title**: Basics of MATLAB – MATLAB Variables & Rules for Variable Names
- **Key Rules & Concepts**:
  - Every variable in MATLAB is internally treated as an array/matrix (scalars are $1 \times 1$ matrices).
  - Variable names must begin with a letter, followed by letters, digits, or underscores (`value_1`).
  - Maximum identifier length is dictated by `namelengthmax`; extra characters are truncated.
  - Identifiers are case-sensitive.
  - CamelCase (e.g., `partNumber`) is preferred over underscores for interoperability with external tools.
  - Reserved keywords cannot be used; built-in function names should not be overwritten.
- **Code & Values**:
  ```matlab
  >> mynum = 6
  mynum =
       6
  >> 6 + 3
  ans =
       9
  >> res = 9 - 2;
  >>
  ```

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-83.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-83.png)
- **Slide Title**: Basics of MATLAB – Commands that Relate to Variables
- **Key Commands & Code**:
  - `who`: Displays the names of currently active workspace variables.
  - `whos`: Displays detailed variable information (name, size, bytes, class).
  - `clear`: Clears all variables from workspace.
  - `clear variablename`: Clears a specified single variable.
  - `clear variablename1 variablename2 ...`: Clears multiple space-delimited variables.
- **Example Trace**:
  ```matlab
  >> who
  >> mynum = 3;
  >> mynum + 5;
  >> who
  Your variables are:
  ans    mynum
  >> clear mynum
  >> who
  Your variables are:
  ans
  ```

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-84.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-84.png)
- **Slide Title**: Basics of MATLAB – Variable Types (Classes)
- **Key Data Types**:
  - **Floats**: `single`, `double` (default numeric type in MATLAB).
  - **Signed integers**: `int8` (1 sign bit, 7 magnitude bits), `int16`, `int32`, `int64`.
  - **Unsigned integers**: `uint8` (8 bits, non-negative values), `uint16`, `uint32`, `uint64`.
  - **Text**: `char` (enclosed in single quotes).
  - **Boolean**: `logical` (`true` or `false`).
  - **Type casting**: Syntax like `int32(num)`.
- **Whos Table Output**:
  ```matlab
  >> num = 6 + 3;
  >> numi = int32(num);
  >> whos
    Name      Size     Bytes  Class      Attributes
    num       1x1          8  double               
    numi      1x1          4  int32                
  ```

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-85.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-85.png)
- **Slide Title**: Basics of MATLAB – Range
- **Key Functions & Values**:
  - Range functions: `intmin('type')` and `intmax('type')` pass the type name as a string.
  - `intmin('int8')` $\rightarrow -128$ (i.e., $-2^7$).
  - `intmax('int8')` $\rightarrow 127$ (i.e., $2^7 - 1$).
  - Recommended general-purpose integer type: `int32`.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-86.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-86.png)
- **Slide Title**: Basics of MATLAB – The Format Function & Scientific or Exponential Notation
- **Formatting Options & Examples**:
  - `format short`: Default (4 decimal places), e.g., `2 * sin(1.4)` $\rightarrow `1.9709`$.
  - `format long`: High precision (15 decimal digits), e.g., `2 * sin(1.4)` $\rightarrow `1.970899459976920`$.
  - `format loose`: Default output spacing with blank lines.
  - `format compact`: Compact display suppressing unnecessary blank lines.
- **Exponential Notation**:
  - `e` denotes power of 10: `2e4` $= 2 \times 10^4 = 20000$.
  - Equivalent code: `2 * 10^4` and `2e4` both output `20000`.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-87.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-87.png)
- **Slide Title**: Basics of MATLAB – Operators
- **Operator Reference Table**:
  - `+`: Addition
  - `-`: Subtraction / Negation
  - `*`: Scalar and matrix multiplication
  - `.*`: Element-wise array multiplication
  - `^`: Scalar and matrix exponentiation
  - `.^`: Element-wise array exponentiation
  - `\`: Matrix left-division ($A \backslash B$)
  - `/`: Matrix right-division ($A / B$)
  - `.\`: Element-wise array left-division
  - `./`: Element-wise array right-division
  - `:`: Colon operator (sequence generation, full row/column)
  - `()`: Parentheses (subscripts, arguments, precedence)
  - `[]`: Brackets (encloses array elements)
  - `.`: Decimal point
  - `...`: Ellipsis (line continuation)
  - `,`: Comma (statement separator, row element separator)
  - `;`: Semicolon (row separator, suppresses command display)
  - `%`: Percent (comment character, format specifier)
  - `'`: Complex conjugate transpose
  - `.'`: Non-conjugated array transpose
  - `=`: Assignment operator
- **Operator Precedence (High to Low)**:
  1. `( )` parentheses
  2. `^` exponentiation
  3. `-` negation
  4. `*`, `/`, `\` multiplication and division
  5. `+`, `-` addition and subtraction

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-88.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-88.png)
- **Slide Title**: Basics of MATLAB – Common Built-in Functions
- **Functions Listed**:
  - `fix`: Truncates toward zero.
  - `floor`: Rounds down toward $-\infty$.
  - `ceil`: Rounds up toward $+\infty$.
  - `round`: Rounds to nearest integer.
  - `mod`: Modulo remainder.
  - `rem`: Remainder; e.g., `rem(13, 5)` returns `3`.
  - `sign`: Returns `1` for positive, `-1` for negative, `0` for zero.
  - `sqrt`: Square root.
  - `nthroot`: Real $n$-th root; e.g., `nthroot(64, 3)` returns `4`.
  - `log(x)`: Natural logarithm (base $e \approx 2.7183$).
  - `log2(x)`: Base-2 logarithm.
  - `log10(x)`: Base-10 logarithm.
  - `exp(n)`: Exponential function $e^n$.
  - `sin`: Sine function (radians).
  - `sind`: Sine function (degrees).

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-89.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-89.png)
- **Slide Title**: Basics of MATLAB – Special Variables and Constants & Characters and Encoding
- **Constants**:
  - `pi`: $\pi \approx 3.14159\dots$
  - `i`, `j`: Imaginary unit $\sqrt{-1}$.
  - `inf`: Infinity ($\infty$).
  - `NaN`: Not a Number (e.g., $0/0$).
- **ASCII Character Encoding & Code Examples**:
  - `double('a')` $\rightarrow `97`$
  - `char(97)` $\rightarrow `'a'`$
  - `double('abcd')` $\rightarrow `97\quad 98\quad 99\quad 100`$
  - `char('abcd' + 1)` $\rightarrow `'bcde'`$

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-90.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-90.png)
- **Slide Title**: Basics of MATLAB – Relational Operators and Expressions
- **Operators & Returns**:
  - `>`: greater than
  - `<`: less than
  - `>=`: greater than or equals
  - `<=`: less than or equals
  - `==`: equality
  - `~=`: inequality
  - Result is boolean/logical: `1` (true) or `0` (false).
- **Examples**:
  - `>> 3 < 5` $\rightarrow `1`$
  - `>> 2 > 9` $\rightarrow `0`$

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-91.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-91.png)
- **Slide Title**: Basics of MATLAB – Logical Operators
- **Operators & Functions**:
  - `||`: Logical OR (scalar short-circuit)
  - `&&`: Logical AND (scalar short-circuit)
  - `~`: Logical NOT
  - `xor`: Exclusive OR function (e.g., `xor(3 < 5, 'a' > 'c')` returns `1`)
- **Operator Precedence (High to Low)**:
  1. `( )` parentheses
  2. `^` power
  3. `-` unary negation, `~` unary not
  4. `*`, `/`, `\` multiplication, division
  5. `+`, `-` addition, subtraction
  6. `<`, `<=`, `>`, `>=`, `==`, `~=` relational
  7. `&&` logical AND
  8. `||` logical OR
  9. `=` assignment
- **Example**: `2 < 4 || 'a' == 'c'` evaluates to true (`1`).

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-92.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-92.png)
- **Slide Title**: Basics of MATLAB – MATLAB Functions and Commands
- **Summary Matrix (40 Built-in Terms)**:
  - **Col 1**: `demo`, `help`, `lookfor`, `doc`, `quit`, `exit`, `namelengthmax`, `who`, `whos`, `clear`, `single`, `double`, `int8`, `int16`, `int32`
  - **Col 2**: `int64`, `uint8`, `uint16`, `uint32`, `uint64`, `intmin`, `intmax`, `char`, `logical`, `true`, `false`, `class`, `format`, `sin`, `abs`
  - **Col 3**: `fix`, `floor`, `ceil`, `round`, `mod`, `rem`, `sign`, `sqrt`, `nthroot`, `log`, `log2`, `log10`, `exp`, `asin`, `sinh`
  - **Col 4**: `asinh`, `sind`, `asind`, `pi`, `i`, `j`, `inf`, `NaN`, `rand`, `rng`, `clock`, `randn`, `randi`, `xor`

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-93.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-93.png)
- **Slide Title**: Basics of MATLAB – Vectors and Matrices
- **Key Concepts & Dimensions ($r \times c$)**:
  - All elements in a MATLAB vector/matrix share the same data type.
  - **Scalar**: $1 \times 1$ (e.g., `[5]`).
  - **Row vector**: $1 \times n$ (e.g., `[5, 88, 3, 11]` is $1 \times 4$).
  - **Column vector**: $n \times 1$ (e.g., `[3; 7; 4]` is $3 \times 1$).
  - **Matrix**: $r \times c$ (e.g., `[9 6 3; 5 7 2]` is $2 \times 3$).

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-94.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-94.png)
- **Slide Title**: Basics of MATLAB – Creating Row Vectors
- **Methods & Code**:
  - **Method 1 (Brackets)**:
    - Space-separated: `>> v = [1  2  3  4]` $\rightarrow 1 \times 4$
    - Comma-separated: `>> v = [1,2,3,4]` $\rightarrow 1 \times 4$
  - **Method 2 (Colon Operator)**:
    - Default unit step: `>> vec = 1:5` $\rightarrow `1\quad 2\quad 3\quad 4\quad 5`$ ($1 \times 5$).
    - Custom step (`start:step:end`): `>> nv = 1:2:9` $\rightarrow `1\quad 3\quad 5\quad 7\quad 9`$ (step of 2).

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-95.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-95.png)
- **Slide Title**: Basics of MATLAB – Creating Column Vectors
- **Methods & Code**:
  - **Direct bracket construction (semicolons)**:
    ```matlab
    >> c = [1; 2; 3; 4]
    c =
         1
         2
         3
         4
    ```
  - **Transposing a row vector (`'`)**:
    ```matlab
    >> r = 1:3;
    >> c = r'
    c =
         1
         2
         3
    ```
  - The colon operator cannot generate a column vector directly; transposition must be applied.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-96.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-96.png)
- **Slide Title**: Basics of MATLAB – Creating Matrices
- **Rules & Examples**:
  - Every row must contain identical numbers of elements.
  - Semicolons separate rows; spaces/commas separate row elements:
    - `mat = [4 3 1; 2 5 6]` $\rightarrow 2 \times 3$ matrix.
    - `m = [1 2 3; 4 5 6; 7 8 9]` $\rightarrow 3 \times 3$ matrix.
  - **Concatenating Vectors**:
    - Row concatenation: `r = [r1, r2]` yields $1 \times 8$; `rMat = [r1; r2]` yields $2 \times 4$.
    - Column concatenation: `c = [c1; c2]` yields $8 \times 1$; `cMat = [c1, c2]` yields $4 \times 2$.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-97.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-97.png)
- **Slide Title**: Basics of MATLAB – Referring to and Modifying Vector Elements
- **Rules & Code**:
  - MATLAB uses 1-based indexing (`index = 1, 2, ..., n`).
  - Given: `newvec = [1 3 5 7 9 3 6 9 12 15]` (indices 1 to 10).
  - **Single element indexing**: `>> newvec(5)` $\rightarrow `9`$.
  - **Range indexing**: `>> b = newvec(4:6)` $\rightarrow `7\quad 9\quad 3`$.
  - **Vector index list**: `>> newvec([1 10 5])` $\rightarrow `1\quad 15\quad 9`$.
  - **Modification**: `>> b(2) = 11` mutates `b` into `7\quad 11\quad 3`.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-98.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-98.png)
- **Slide Title**: Basics of MATLAB – Referring to and Modifying Matrix Elements
- **Rules & Code**:
  - Subscripted indexing format: `matrix(row, col)`.
  - Given `mat = [2:4; 3:5]`:
    $$\text{mat} = \begin{bmatrix} 2 & 3 & 4 \\ 3 & 4 & 5 \end{bmatrix}$$
  - **Single element**: `>> mat(2,3)` $\rightarrow `5`$.
  - **Submatrix block**: `>> mat(1:2, 2:3)` $\rightarrow \begin{bmatrix} 3 & 4 \\ 4 & 5 \end{bmatrix}$.
  - **Element reassignment**: `>> mat(1,2) = 11` updates row 1, col 2 $\rightarrow \begin{bmatrix} 2 & 11 & 4 \\ 3 & 4 & 5 \end{bmatrix}$.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-99.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-99.png)
- **Slide Title**: Basics of MATLAB – Dimensions
- **Key Functions & Logic**:
  - `length(vec)`: Returns the number of elements in a vector.
  - `size(vec_or_mat)`: Returns dimensions `[rows, cols]`.
  - Multiple output capture: `[r, c] = size(mat)` stores row count in `r` and column count in `c`.
  - For a 2D matrix, `length(mat)` returns $\max(\text{rows}, \text{columns})$.
- **Example Traces**:
  - For `vec = -2:1` (length 4): `length(vec)` $\rightarrow 4$; `size(vec)` $\rightarrow `1\quad 4`$.
  - For `mat` with 3 rows and 2 columns: `[r, c] = size(mat)` $\rightarrow r = 3, c = 2$; `length(mat)` $\rightarrow 3$.

---

#### [M1-MAIN-Introduction to Modeling and Simulation-page-100.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M1-MAIN-Introduction%20to%20Modeling%20and%20Simulation-page-100.png)
- **Slide Title**: Basics of MATLAB – Dimensions (numel)
- **Key Function & Best Practices**:
  - `numel(A)`: Returns the total count of elements in any array (for vectors, equal to `length`; for matrices, equal to $\text{rows} \times \text{cols}$).
  - Code:
    - `vec = 9:-2:1` $\rightarrow$ `numel(vec)` returns `5`.
    - `mat = [3:2:7; 9 33 11]` ($2 \times 3$ matrix) $\rightarrow$ `numel(mat)` returns `6`.
  - **Recommendation**:
    - Use `length` or `numel` for vectors.
    - Use `size(mat)` (storing results into two variables) for matrices.

---

### Possible slide errors

1. **Slide 84 – Inaccurate definition of unsigned integers**:
   - The slide states: `uint8 – uses eight bits (sign not stored, actual number must only be positive)`.
   - *Why it is wrong*: Unsigned integers can also be zero (`0` to `255`), so the value must be **non-negative**, not strictly positive.

2. **Slide 87 – Typographical errors in operator glyphs**:
   - In the operators table, the transpose operator is rendered as an en-dash `–` instead of a single quote `'`.
   - More severely, nonconjugated transpose is written as `–'` (dash followed by single quote) instead of `.'` (dot followed by single quote). In MATLAB, `-'` is invalid syntax for an operator.

3. **Slide 88 – Inaccurate definition of `sign`**:
   - The slide states: `sign -> returns 1 if the argument is positive. Otherwise returns -1.`
   - *Why it is wrong*: If the argument is `0`, MATLAB's `sign(0)` returns `0`, not `-1`.

4. **Slide 88 – Mathematically incorrect explanation of `log(x)`**:
   - The slide states: `log(x) -> returns the natural logarithm ( equals e which has a value of 2.7183)`.
   - *Why it is wrong*: $\log(x)$ does not "equal $e$"; it calculates the logarithm to the base $e$ ($\ln(x)$). $\log(x) = 1$ only when $x = e$.

5. **Slide 78 – Grammatical typos in learning objectives**:
   - The slide writes: `"Use build-in functions to simplify codes involving vectors and matrices."`
   - *Why it is wrong*: It uses `"build-in"` instead of `"built-in"` and the non-standard plural `"codes"` instead of `"code"`.

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-101.png`
- **Slide Title**: Basics of MATLAB (Changing Dimensions – Built-in Functions)
- **Key Facts**:
  - The `reshape` function reorganizes the elements of a matrix into specified new dimensions without altering the total number of elements.
  - MATLAB processes elements in column-major order during reshaping.
- **Code & Output**:
  ```matlab
  >> mat = randi(100, 3, 4)
      14    61     2    94
      21    28    75    47
      20    20    45    42

  >> reshape(mat, 2, 6)
  ans =
      14    20    28     2    45    47
      21    61    20    75    94    42
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-102.png`
- **Slide Title**: Basics of MATLAB (Changing Dimensions – Built-in Functions)
- **Key Facts**:
  - `fliplr(mat)`: Flips a matrix horizontally (left to right), swapping columns.
  - `flipud(mat)`: Flips a matrix vertically (up to down), swapping rows.
- **Code & Output**:
  ```matlab
  >> mat = randi(100, 3, 4)
      14    61     2    94
      21    28    75    47
      20    20    45    42

  >> fliplr(mat)
  ans =
      94     2    61    14
      47    75    28    21
      42    45    20    20

  >> flipud(mat)
  ans =
      20    20    45    42
      21    28    75    47
      14    61     2    94
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-103.png`
- **Slide Title**: Basics of MATLAB (Changing Dimensions – Built-in Functions)
- **Key Facts**:
  - `rot90(mat)`: Rotates a matrix counterclockwise by $90^\circ$.
  - The top-right value moves to the top-left corner, and the rightmost column becomes the first row.
- **Code & Output**:
  ```matlab
  >> mat = randi(100, 3, 4)
      14    61     2    94
      21    28    75    47
      20    20    45    42

  >> rot90(mat)
  ans =
      94    47    42
       2    75    45
      61    28    20
      14    21    20
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-104.png`
- **Slide Title**: Basics of MATLAB (Changing Dimensions – Built-in Functions)
- **Key Facts**:
  - `repmat(mat, m, n)` replicates and tiles a matrix `mat` across $m$ rows and $n$ columns of blocks.
- **Code & Output**:
  ```matlab
  >> intmat = randi(100, 2)
  intmat =
      50    34
      96    59

  >> repmat(intmat, 3, 2)
  ans =
      50    34    50    34
      96    59    96    59
      50    34    50    34
      96    59    96    59
      50    34    50    34
      96    59    96    59
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-105.png`
- **Slide Title**: Basics of MATLAB (Empty Vectors)
- **Key Facts**:
  - An empty vector stores no values and is initialized using empty brackets `[]`.
  - Its length is 0.
  - Elements can be appended dynamically via concatenation.
- **Code & Output**:
  ```matlab
  >> evec = []
  evec =
      []
  >> length(evec)
  ans =
       0
  >> evec = [evec 4]
  evec =
       4
  >> evec = [evec 11]
  evec =
       4    11
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-106.png`
- **Slide Title**: Basics of MATLAB (Deleting Elements from a Vector)
- **Key Facts**:
  - Assigning `[]` to a vector index removes that element, automatically re-indexing remaining elements.
  - Individual elements cannot be deleted from a 2D matrix using index assignment (`mat(r, c) = []`) because matrices must preserve rectangular dimensionality.
- **Code & Output**:
  ```matlab
  >> vec = 4:8
  vec =
       4     5     6     7     8
  >> vec(3) = []
  vec =
       4     5     7     8

  >> mat = [7 9 8; 4 6 5]
  mat =
       7     9     8
       4     6     5
  >> mat(1,2) = [];
  Subscripted assignment dimension mismatch.
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-107.png`
- **Slide Title**: Basics of MATLAB (Vectors and Matrices as Function Arguments)
- **Key Facts**:
  - Standard mathematical functions applied to vectors/matrices evaluate element-by-element, preserving output shape.
  - `sin()` accepts arguments in radians.
  - `sign()` returns `-1` (negative), `0` (zero), or `1` (positive).
- **Code & Output**:
  ```matlab
  >> vec = -2:1
  vec =
      -2    -1     0     1
  >> sinvec = sin(vec)
  sinvec =
     -0.9093   -0.8415         0    0.8415

  >> mat = [0 4 -3; -1 0 2]
  mat =
       0     4    -3
      -1     0     2
  >> sign(mat)
  ans =
       0     1    -1
      -1     0     1
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-108.png`
- **Slide Title**: Basics of MATLAB (Vectors and Matrices as Function Arguments)
- **Key Facts**:
  - `min()`, `max()`, `sum()`, and `prod()` return scalar aggregate values when applied to a vector.
  - `cumsum()` and `cumprod()` calculate running/cumulative totals and preserve the vector length.
- **Code & Output**:
  ```matlab
  >> vec1 = 1:5;
  >> vec2 = [3 5 8 2];
  >> min(vec1)       % ans = 1
  >> sum(vec1)       % ans = 15
  >> max(vec2)       % ans = 8
  >> prod(vec2)      % ans = 240

  >> cumsum(vec1)    % ans = [1 3 6 10 15]
  >> cumsum(vec2)    % ans = [3 8 16 18]
  >> cumprod(vec1)   % ans = [1 2 6 24 120]
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-109.png`
- **Slide Title**: Basics of MATLAB (Vectors and Matrices as Function Arguments)
- **Key Facts**:
  - By default, `min`, `max`, `sum`, and `prod` operate column-wise on matrices.
  - An $r \times c$ input matrix results in a $1 \times c$ row vector of column statistics.
- **Code & Output**:
  ```matlab
  >> mat = randi([1 20], 3, 5)
  mat =
       3    16     1    14     8
       9    20    17    16    14
      19    14    19    15     4

  >> max(mat)
  ans =
      19    20    19    16    14

  >> sum(mat)
  ans =
      31    50    37    45    26
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-110.png`
- **Slide Title**: Basics of MATLAB (Vectors and Matrices as Function Arguments)
- **Key Facts**:
  - To apply aggregate functions across rows, one approach is transposing the matrix first (`mat'`).
  - Output is formatted as a row vector ($1 \times r$).
- **Code & Output**:
  ```matlab
  >> max(mat')
  ans =
      16    20    19

  >> sum(mat')
  ans =
      42    76    71
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-111.png`
- **Slide Title**: Basics of MATLAB (Vectors and Matrices as Function Arguments)
- **Key Facts**:
  - MATLAB defines columns as dimension 1 (default) and rows as dimension 2.
  - For `sum` and `prod`, row-wise operation is specified via the 2nd argument: `sum(mat, 2)`.
  - For `min` and `max`, row-wise operation requires an empty vector as the 2nd argument and dimension as the 3rd: `max(mat, [], 2)`.
  - Unlike transposing (which returns a $1 \times r$ row vector), specifying dimension 2 returns an $r \times 1$ column vector.
- **Code & Output**:
  ```matlab
  >> max(mat, [], 2)
  ans =
      16
      20
      19

  >> sum(mat, 2)
  ans =
      42
      76
      71
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-112.png`
- **Slide Title**: Basics of MATLAB (Scalar Operations on Vectors and Matrices / Scalar Multiplication)
- **Key Facts**:
  - Multiplying or dividing a vector or matrix by a scalar applies the operation to every element.
- **Code & Output**:
  ```matlab
  >> v = [3 7 2 1];
  >> v = v*3
  v =
       9    21     6     3

  >> v = [3 7 2 1];
  >> v/2
  ans =
      1.5000    3.5000    1.0000    0.5000

  >> mat = [4:6; 3:-1:1]
  mat =
       4     5     6
       3     2     1
  >> mat * 2
  ans =
       8    10    12
       6     4     2
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-113.png`
- **Slide Title**: Vectors and Matrices (Array Operations on Vectors and Matrices)
- **Key Facts**:
  - Array operations execute element-by-element.
  - Participating arrays must have matching dimensions.
- **Code & Output**:
  ```matlab
  >> v1 = 2:5;                % [2 3 4 5]
  >> v2 = [33 11 5 1];
  >> v1 + v2
  ans =
      35    14     9     6

  >> mata = [5:8; 9:-2:3];
  >> matb = reshape(1:8, 2, 4);
  >> mata - matb
  ans =
       4     3     2     1
       7     3    -1    -5
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-114.png`
- **Slide Title**: Vectors and Matrices (Array Operations on Vectors and Matrices)
- **Key Facts**:
  - Element-wise operations based on multiplication (multiplication, division, exponentiation) require a dot prefix: `.*`, `./`, `.^`.
- **Code & Output**:
  ```matlab
  >> v = [3 7 2 1];
  >> v .^ 2
  ans =
       9    49     4     1

  >> v1 = 2:5;
  >> v2 = [33 11 5 1];
  >> v1 .* v2
  ans =
      66    33    20     5
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-115.png`
- **Slide Title**: Vectors and Matrices (Array Operations on Vectors and Matrices / Transpose of a Matrix)
- **Key Facts**:
  - The apostrophe (`'`) operator transposes rows into columns and vice versa.
- **Code & Output**:
  ```matlab
  a = [ 10 12 23 ; 14 8 6; 27 8 9]
  b = a'

  a =
      10    12    23
      14     8     6
      27     8     9

  b =
      10    14    27
      12     8     8
      23     6     9
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-116.png`
- **Slide Title**: Basics of MATLAB (Matrix Multiplication)
- **Key Facts & Formulas**:
  - For $[A] \times [B]$ to be valid, inner dimensions must match: columns of $A$ = rows of $B$.
  - Dimension relation:
    $$[A]_{m \times n} [B]_{n \times p} = [C]_{m \times p}$$
  - Entry-wise formula:
    $$c_{ij} = \sum_{k=1}^n a_{ik} b_{kj}$$

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-117.png`
- **Slide Title**: Basics of MATLAB (Matrix Multiplication)
- **Key Facts**:
  - Matrix multiplication in MATLAB uses the standard `*` operator.
  - Multiplies a $2 \times 3$ matrix by a $3 \times 4$ matrix to produce a $2 \times 4$ matrix.
- **Formula & Code**:
  $$\begin{bmatrix} 3 & 8 & 0 \\ 1 & 2 & 5 \end{bmatrix} * \begin{bmatrix} 1 & 2 & 3 & 1 \\ 4 & 5 & 1 & 2 \\ 0 & 2 & 3 & 0 \end{bmatrix} = \begin{bmatrix} 35 & 46 & 17 & 19 \\ 9 & 22 & 20 & 5 \end{bmatrix}$$
  ```matlab
  >> A = [3 8 0; 1 2 5];
  >> B = [1 2 3 1; 4 5 1 2; 0 2 3 0];
  >> C = A*B
  C =
      35    46    17    19
       9    22    20     5
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-118.png`
- **Slide Title**: Basics of MATLAB (Determinant of a Matrix)
- **Key Facts**:
  - The determinant is computed using `det(A)` on square matrices.
- **Code & Output**:
  ```matlab
  a = [ 1 2 3; 2 3 4; 1 2 5]
  det(a)

  a =
       1     2     3
       2     3     4
       1     2     5
  ans = -2
  ```

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-119.png`
- **Slide Title**: Formative Assessment 1
- **Key Facts**:
  - Directs students to check Canvas for assessment instructions.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-120.png`
- **Slide Title**: Summative Assessment 1
- **Key Facts**:
  - Directs students to check Canvas for assessment instructions.

---

### `img/M1-MAIN-Introduction to Modeling and Simulation-page-121.png`
- **Slide Title**: References
- **Key Facts & Citations**:
  - Online resource: `www.tutorialspoint.com`
  - Textbook: Attaway, Stormy (2013). *MATLAB ®. A Practical Introduction to Programming and Problem Solving*, Third Edition. Elsevier, Inc.

---

### Possible slide errors

1. **Slides 109, 110, and 111**:
   - **Why it is wrong/misleading**: In all three slides, the code snippet begins with `>> mat = randi([1 20], 3, 5)` and displays the exact same random output matrix. In an actual MATLAB session, re-running `randi` without resetting the random number generator seed will produce different pseudo-random values each time. The slides intended to reuse the same variable across demonstrations, but re-showing the call as if it produces identical numbers on fresh calls is misleading.
2. **Slide 112**:
   - **Why it is an error**: The section header is named **"Scalar Multiplication"**, but the slide explicitly explains and includes an example of **scalar division** (`v/2`). It should be titled "Scalar Multiplication and Division" or kept under "Scalar Operations".
3. **Slide 115**:
   - **Why it is an error**: The slide header reads **"Array Operations on Vectors and Matrices"**, but the topic displayed is **"Transpose of a Matrix"**. Transpose is a unary matrix shape/structural rearrangement operation, not an element-by-element binary array operation as defined on Slide 113.
4. **Slides 115 and 118**:
   - **Why it is inconsistent**: Unlike all other interactive MATLAB command prompt examples throughout the deck (which use the `>>` prompt), Slides 115 and 118 omit the `>>` prompt in their input boxes, creating inconsistent syntax formatting.
