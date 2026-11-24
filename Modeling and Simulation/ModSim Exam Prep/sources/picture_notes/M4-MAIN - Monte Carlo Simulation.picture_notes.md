### Study Notes: Module 4 – Monte Carlo Simulation

---

#### 1. [img/M4-MAIN - Monte Carlo Simulation-page-1.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-1.png)
* **Title:** Modeling and Simulation
* **Key Facts:** Course title slide featuring FEU institutional branding (FEU Alabang, FEU Diliman, FEU Tech) and motto ("Technology Driven by Innovation").

---

#### 2. [img/M4-MAIN - Monte Carlo Simulation-page-2.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-2.png)
* **Title:** MODULE 4: MONTE CARLO SIMULATION
* **Key Facts:** Module banner announcing the core topic of Monte Carlo Simulation.

---

#### 3. [img/M4-MAIN - Monte Carlo Simulation-page-3.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-3.png)
* **Title:** SUBTOPIC 1: CONCEPTS ON MONTE CARLO SIMULATION
* **Key Facts:** Section divider introducing fundamental definitions, principles, and models.

---

#### 4. [img/M4-MAIN - Monte Carlo Simulation-page-4.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-4.png)
* **Title:** OBJECTIVES
* **Key Facts:**
  * Understand Monte Carlo Simulation concepts and mechanics.
  * Identify distinct Monte Carlo simulation methods.
  * Understand and articulate the role and importance of sensitivity analysis.

---

#### 5. [img/M4-MAIN - Monte Carlo Simulation-page-5.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-5.png)
* **Title:** Monte Carlo Simulations
* **Key Facts & Quotes:**
  * **Origin:** Developed in the 1940s during atomic bomb research.
  * **Nature:** A broad class of computational algorithms that rely on repeated random sampling.
  * **Characteristics:** Described as "not a statistical tool" in the traditional sense, but an algorithmic technique that yields approximate solutions.
  * **Application Criteria:** Primarily used when analytical or direct numerical solutions are intractable or nonexistent; humorously noted as usable by the "Lazy Scientist™" even when analytical solutions exist.
  * **Source:** Stéphane Paltani (ISDC Data Center for Astrophysics, University of Geneva).

---

#### 6. [img/M4-MAIN - Monte Carlo Simulation-page-6.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-6.png)
* **Title:** Monte Carlo Simulations
* **Key Facts:**
  * **Alternative Name:** Monte Carlo Method.
  * **Location & Era:** Los Alamos National Laboratory (NM, USA) in the 1940s.
  * **Key Contributors:** Stanislaw Ulam (noted as "Ulman"), Enrico Fermi, John von Neumann, and Nicholas Metropolis.
  * **Mechanisms:** Used repeated simulations of atomic physics models to account for numerous uncertain input variables. Aggregated random input iterations produce a statistical output representing the physical system.
  * **Claim:** Positioned as superior to purely deterministic models when handling real-world systems with inherently random inputs.

---

#### 7. [img/M4-MAIN - Monte Carlo Simulation-page-7.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-7.png)
* **Title:** Monte Carlo Simulations
* **Key Facts:**
  * **Definition:** A computerized mathematical procedure generating random sample data drawn from known probability distributions to execute numerical experiments.
  * **Primary Domains:** Quantitative risk analysis and decision-making problems.
  * **Industries:** Widely applied in finance, project management, energy, manufacturing, engineering, R&D, insurance, oil & gas, and transportation.

---

#### 8. [img/M4-MAIN - Monte Carlo Simulation-page-8.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-8.png)
* **Title:** Monte Carlo Models
* **Key Models Illustrated:**
  1. **Simple Monte Carlo:** A single input source ($N$) directly generates independent outputs/variables ($A, B, C$).
  2. **Mixture Modelling:** Multiple sub-populations or distribution mixtures generate grouped subsets of variables ($A, B, C$).
  3. **Two Stage - Monte Carlo:** Hierarchical structure where input $N$ drives first-stage outputs ($A, B, C$), and node $C$ subsequently feeds a second stage ($D, E$).
  4. **Markov Chain:** Chain-linked stochastic states ($A \to B \to C \to D$) with state-to-state transition probabilities and feedback loops.

---

#### 9. [img/M4-MAIN - Monte Carlo Simulation-page-9.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-9.png)
* **Title:** Monte Carlo Simulations – Important Characteristics
* **Key Properties Listed:**
  * Output must generate random samples.
  * The input probability distribution must be known.
  * States: "Its result must be known while performing an experiment." *(See slide error notes below).*

---

#### 10. [img/M4-MAIN - Monte Carlo Simulation-page-10.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-10.png)
* **Title:** Monte Carlo Simulations – Advantages / Disadvantages
* **Key Tradeoffs:**
  * **Advantages:** Straightforward to implement; provides computerized statistical sampling; generates approximate solutions for intractable problems; handles both stochastic and deterministic problem formulations.
  * **Disadvantages:** Computationally demanding and time-consuming due to the large sample size needed for high precision; results are approximations rather than exact analytical values.

---

#### 11. [img/M4-MAIN - Monte Carlo Simulation-page-11.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-11.png)
* **Title:** Monte Carlo Simulations - Applications: Numerical integration
* **Key Facts & Formulas:**
  * Numerical integration is the single most common application of Monte Carlo methods.
  * Avoids fixed-grid evaluation because:
    1. **Curse of dimensionality:** A fixed grid in $D$ dimensions scales exponentially, requiring $N^D$ evaluation points.
    2. Fixed grid algorithms require selecting a rigid step size beforehand.

---

#### 12. [img/M4-MAIN - Monte Carlo Simulation-page-12.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-12.png)
* **Title:** Monte Carlo Simulations - Applications: Error estimation
* **Key Facts & Formulas:**
  * For an arbitrary probability distribution with a proper random sampler ($x \sim f(x)$), Monte Carlo evaluates:
    * Distribution properties (mean, variance, higher moments).
    * Confidence intervals:
      $$P(x > \alpha) = \int_{\alpha}^{\infty} f(x)\,dx$$
    * Composition of distributions (e.g., given $P(x)$, find $P(h(x))$ where $h(x) = x^2, \cos(x) - \sin(x), \dots$).
  * Core insight: all these operations reduce to definite integrals.

---

#### 13. [img/M4-MAIN - Monte Carlo Simulation-page-13.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-13.png)
* **Title:** Monte Carlo Simulations - Applications: Optimization problems
* **Key Facts:**
  * Standard deterministic/gradient numerical optimization risks trapping algorithms inside local minima.
  * Monte Carlo approaches allow stochastic jumps ("permitting random exit") out of local basins to discover deeper or global minima (analogous to simulated annealing).

---

#### 14. [img/M4-MAIN - Monte Carlo Simulation-page-14.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-14.png)
* **Title:** Monte Carlo Simulations - Applications: Numerical simulations
* **Key Facts:**
  * In astrophysics, radiative transfer is the most prominent Monte Carlo application.
  * Simulates physical interactions such as input rays, iron fluorescence ($\text{Fe K}\alpha$), Compton shoulders, and scattered continua.
  * Ideal for particle physics and high-energy astrophysics because quantum/collisional processes are naturally discrete and stochastic.

---

#### 15. [img/M4-MAIN - Monte Carlo Simulation-page-15.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-15.png)
* **Title:** Monte Carlo Simulations - The Monte Carlo Method: Overview of the method
* **Key Four-Step Methodology:**
  1. Determine statistical properties of input variables.
  2. Generate numerous input sets matching those distributions.
  3. Execute deterministic computations on each input set.
  4. Perform statistical aggregation and analysis on the collective outputs.
* **Convergence Rate:**
  $$\text{Error} \propto \frac{1}{\sqrt{N}}$$

---

#### 16. [img/M4-MAIN - Monte Carlo Simulation-page-16.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-16.png)
* **Title:** Monte Carlo Simulations - The Monte Carlo Method: Flow Diagram
* **Flowchart Architecture:**
  * `Distributing Input` $\to$ `Step 1: Sampling of random variables (Random variables sample generation)` $\to$ `Input variable`
  * Model Evaluation block: `Analyzing the model; F = g(X)`
  * `Step 2: Experimenting numerical problems (Leads to performance analysis)` $\to$ `Output Variable`
  * `Step 3: Performing statistical analysis on output result` $\to$ `Output result based on statistical`

---

#### 17. [img/M4-MAIN - Monte Carlo Simulation-page-17.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-17.png)
* **Title:** Monte Carlo Simulations – The Monte Carlo Method: Four-step process
* **Core Steps Formalized:**
  1. Define a distribution of possible inputs for each random variable.
  2. Generate inputs randomly from those distributions.
  3. Perform a deterministic computation with that set of inputs.
  4. Aggregate individual run outputs into the final overall result.

---

#### 18. [img/M4-MAIN - Monte Carlo Simulation-page-18.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-18.png)
* **Title:** Monte Carlo Simulations – The Monte Carlo Method: Five Core Components
* **Key Components:**
  1. **Probability distribution functions (pdfs):** Characterizing each random variable.
  2. **Random number generator:** Source of uniform/stochastic variates.
  3. **Sampling rule:** Exact prescription used to draw values from the pdfs.
  4. **Scoring:** Rule/function combining output observations into aggregated estimates.
  5. **Error estimation:** Quantitative formulation measuring statistical uncertainty as a function of iteration count $N$ and system parameters.

---

#### 19. [img/M4-MAIN - Monte Carlo Simulation-page-19.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-19.png)
* **Title:** Monte Carlo Simulations – Example: Determining the Value of PI
* **Key Setup:**
  * Uses the geometric ratio of a circle's area relative to a circumscribed bounding box.
  * **Step 1:** Establish the domain of inputs by circumscribing a quarter unit circle arc ($r = 1$) within a unit square ($[0,1] \times [0,1]$).

---

#### 20. [img/M4-MAIN - Monte Carlo Simulation-page-20.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-20.png)
* **Title:** Monte Carlo Simulations – Example: Determining the Value of PI
* **Execution Steps:**
  * **Step 2:** Uniformly sample random coordinates $(x, y)$ inside the unit square ($0 \le x, y \le 1$) and record each point.
  * **Step 3:** Repeat Step 2 for a large sample count (illustrated by scatter points filling the square).

---

#### 21. [img/M4-MAIN - Monte Carlo Simulation-page-21.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-21.png)
* **Title:** Monte Carlo Simulations – Example: Determining the Value of PI
* **Analysis & Formula:**
  * **Step 4:** Count the points falling within the quarter circle ($x^2 + y^2 \le 1$) versus the total points in the square.
  * **Geometric Ratio:**
    $$\frac{\text{\# of dots inside circle}}{\text{\# of dots inside square}} = \frac{\frac{1}{4}\pi r^2}{r^2} = \frac{1}{4}\pi$$
  * **Pi Estimation:**
    $$\pi \approx 4 \times \frac{\text{\# of dots inside quarter circle}}{\text{\# of dots inside square}}$$

---

#### 22. [img/M4-MAIN - Monte Carlo Simulation-page-22.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-22.png)
* **Title:** Monte Carlo Simulations – Sensitivity Analysis
* **Key Concepts:**
  * **Definition:** Apportioning the uncertainty in model outputs to specific sources of input uncertainty.
  * **Objective:** Identifying which input random variables exert the strongest impact on target output distributions.

---

#### 23. [img/M4-MAIN - Monte Carlo Simulation-page-23.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-23.png)
* **Title:** Monte Carlo Simulations – Sensitivity Analysis: Importance of Sensitivity Analysis
* **Key Facts:**
  * **Benefits:** Detects model specification flaws, pinpoints sensitive input bounds, guides experimental/research priorities, and enables model simplification.
  * **Derivative-Based Approaches:**
    * Most prevalent classical sensitivity method; computationally efficient.
    * **Major Flaw:** Only valid *locally* at the specific evaluation point. While fine for strictly linear systems, it fails to capture nonlinear system behavior.

---

#### 24. [img/M4-MAIN - Monte Carlo Simulation-page-24.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-24.png)
* **Title:** Formative Assessment 5
* **Key Facts:** Directs students to check Canvas for assignment details and instructions.

---

#### 25. [img/M4-MAIN - Monte Carlo Simulation-page-25.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M4-MAIN%20-%20Monte%20Carlo%20Simulation-page-25.png)
* **Title:** Summative Assessment 4
* **Key Facts:** Directs students to check Canvas for instructions regarding the module summative assessment.

---

### Possible slide errors

1. **Slide 6 – Typo in Historical Name:**
   * **Error:** Lists the co-inventor as *"Stanislaw Ulman"*.
   * **Why it is wrong:** The mathematician was **Stanislaw Ulam** (famous for the Ulam spiral and Teller–Ulam design).

2. **Slide 6 – Questionable Superiority Claim:**
   * **Error:** Asserts Monte Carlo is *"Superior to a deterministic simulation system since it has input variables that are random."*
   * **Why it is wrong:** Neither paradigm is universally superior. Deterministic models are preferable when governing laws are known, precise, and exact analytical or numerical solutions exist without introducing random sampling noise. Stochastic models are suited specifically when inputs/systems have uncertainty.

3. **Slide 9 – Factual Contradiction in Core Characteristics:**
   * **Error:** States *"Its result must be known while performing an experiment."*
   * **Why it is wrong:** In simulation experiments, the outcome is inherently **unknown**; simulation is performed specifically to estimate unknown distributions or values. The deterministic model transfer function $F = g(X)$ is known, but the experiment's result is not.

4. **Slide 5 – Misleading Method Classification:**
   * **Error:** Claims Monte Carlo simulations *"are not a statistical tool"*.
   * **Why it is wrong:** Monte Carlo methods are grounded entirely in mathematical statistics and probability (e.g., Central Limit Theorem, Law of Large Numbers). Later slides (e.g., Slides 10, 15, and 16) explicitly refer to "statistical sampling" and "performing statistical analysis" on results.

5. **Slide 16 – Incomplete Label Grammar:**
   * **Error:** The terminating oval in the flowchart reads *"Output result based on statistical"*.
   * **Why it is wrong:** The phrase is grammatically incomplete and truncated (missing a noun such as *"statistical analysis"* or *"statistical distribution"*).

6. **Slide 19 & 21 – Geometric Terminology & Formula Labeling:**
   * **Error in Slide 19:** Describes the setup as *"an arc of radius one circumscribed by a square"*.
   * **Why it is wrong:** Geometrically, the square is *circumscribed about* the arc (or the quarter circle is *inscribed* in the square), not the other way around.
   * **Error in Slide 21:** The ratio formula numerator is labeled `"# of dots inside circle"`.
   * **Why it is wrong:** The geometry shown is strictly a **quarter circle** (a quadrant), which is why the area in the formula is $\frac{1}{4}\pi r^2$, not the full circle area $\pi r^2$. Labeling it as "quarter circle" avoids student confusion.

### Study Notes: MATLAB File I/O & Plotting (Slides 26–50)

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-26.png`
- **Slide Title**: References
- **Key Facts & Citations**:
  - **Online**: `https://www.tutorialspoint.com/`
  - **Textbook**: Sokolowski, John A. & Banks, Catherine M. (2010). *Modeling and Simulation Fundamentals Theoretical Underpinnings and Practical Domains*. John Wiley & Sons.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-27.png`
- **Slide Title**: MATLAB File Input and Output & 2D/3D Plotting (Modeling and Simulation)
- **Key Facts**: Section banner introducing file input/output and 2D/3D plotting in MATLAB.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-28.png`
- **Slide Title**: Subtopic 2: MATLAB Programming: File Input and Output & 2D / 3D Plotting
- **Key Facts**: Subtopic divider slide.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-29.png`
- **Slide Title**: File Input and Output
- **Key Facts**: Divider slide introducing File Input and Output topics.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-30.png`
- **Slide Title**: OBJECTIVES
- **Key Facts**:
  - Build MATLAB scripts to export/save data to external files.
  - Build MATLAB scripts to import/read data from external files.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-31.png`
- **Slide Title**: File Input and Output — Writing Data to a File
- **Key Facts & Options**:
  - Common data export methods in MATLAB:
    - Delimited ASCII rectangular files from numeric arrays.
    - Session keystroke/output logging using diary files.
    - Low-level formatted text output using functions like `fprintf`.
    - Custom file exporting via MEX-files (C/C++ or Fortran).
    - Spreadsheet export (e.g., Excel).

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-32.png`
- **Slide Title**: File Input and Output — Writing Data to a File
- **Key Facts & Syntax**:
  - Two ways to export numeric arrays to delimited ASCII:
    1. `save filename matrixvariablename -ascii`
    2. `dlmwrite('my_data.out', num_array, 'dlm_char')`
  - Notes:
    - Saving character arrays with `-ascii` writes numeric ASCII codes instead of literal text.
    - The `save` command overwrites the target file by default from the beginning.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-33.png`
- **Slide Title**: File Input and Output — Writing Data to a File (Example 1)
- **Code & Output**:
  ```matlab
  >> mymat = rand(2,3)
  mymat =
      0.4565    0.8214    0.6154
      0.0185    0.4447    0.7919
  >> save testfile.dat mymat -ascii
  >> type testfile.dat
     4.5646767e-001  8.2140716e-001  6.1543235e-001
     1.8503643e-002  4.4470336e-001  7.9193704e-001
  ```
- **Key Facts**: Using `save ... -ascii` exports values in 8-digit scientific floating-point notation.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-34.png`
- **Slide Title**: File Input and Output — Writing Data to a File (Example 2)
- **Code & File Values**:
  ```matlab
  num_array = [ 1 2 3 4 ; 4 5 6 7 ; 7 8 9 0];
  dlmwrite('array_data2.out', num_array, ' ');
  type array_data2.out
  ```
  File contents (`array_data2.out`):
  ```text
  1 2 3 4
  4 5 6 7
  7 8 9 0
  ```
- **Key Facts**: `dlmwrite` allows specifying custom delimiters (a single space `' '` here).

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-35.png`
- **Slide Title**: File Input and Output — Writing Data to a File (Example 3)
- **Code & File Values**:
  ```matlab
  >> mat2 = rand(3,3)
  >> save testfile.dat mat2 -ascii -append
  ```
  File contents (`testfile.dat` after appending):
  ```text
  0.4565    0.8214    0.6154
  0.0185    0.4447    0.7919
  0.9218    0.4057    0.4103
  0.7382    0.9355    0.8936
  0.1763    0.9169    0.0579
  ```
- **Key Facts**: The `-append` flag adds rows to an existing ASCII file rather than overwriting it.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-36.png`
- **Slide Title**: File Input and Output — Writing Data to a File (Example 4)
- **Code & File Values**:
  ```matlab
  h = 'hello';
  save textdata.out h -ascii
  type textdata.out
  ```
  Output in `textdata.out`:
  ```text
  1.0400000e+02   1.0100000e+02   1.0800000e+02   1.0800000e+02   1.1100000e+02
  ```
- **Key Facts**: Confirms `-ascii` writes raw ASCII codes for characters (`'h'=104`, `'e'=101`, `'l'=108`, `'l'=108`, `'o'=111`).

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-37.png`
- **Slide Title**: File Input and Output — Reading from a File (Example 1)
- **Key Facts & Code**:
  - `load` creates a variable matching the file's base name.
  - Requires consistent row lengths (rectangular data).
  ```matlab
  >> clear
  >> load testfile.dat
  >> who
  Your variables are:
  testfile
  >> testfile
  testfile =
      0.4565    0.8214    0.6154
      0.0185    0.4447    0.7919
      0.9218    0.4057    0.4103
      0.7382    0.9355    0.8936
      0.1763    0.9169    0.0579
  ```

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-38.png`
- **Slide Title**: File Input and Output — Reading from a File (Example 2)
- **Data (`timetemp.dat`)**:
  ```text
  0    3    6    9    12   15   18   21
  55.5 52.4 52.6 55.7 75.6 77.7 70.3 66.6
  ```
- **Code (`timetempprob.m`)**:
  ```matlab
  load timetemp.dat
  time = timetemp(1,:);
  temp = timetemp(2,:);
  plot(time,temp,'k*')
  xlabel('Time')
  ylabel('Temperature')
  title('Temperatures one afternoon')
  ```
- **Key Facts**: Extracts rows using indexing (`(1,:)`, `(2,:)`) and plots them with black asterisks (`'k*'`).

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-39.png`
- **Slide Title**: References
- **Key Facts & Citations**:
  - **Online**: `www.tutorialspoint.com`
  - **Textbook**: Attaway, Stormy (2013). *MATLAB ®. A Practical Introduction to Programming and Problem Solving Third Edition*. Elsevier, Inc.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-40.png`
- **Slide Title**: 2D & 3D Plotting
- **Key Facts**: Section title slide for graphics and plotting functions.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-41.png`
- **Slide Title**: OBJECTIVES
- **Key Facts**:
  - Learn to produce 2D plots.
  - Learn to produce 3D plots.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-42.png`
- **Slide Title**: Plotting Commands
- **Key Facts**: Subtopic divider slide for basic plot commands.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-43.png`
- **Slide Title**: Plotting Commands
- **Table Values**:
  - `axis`: Sets axis limits.
  - `fplot`: Intelligent function plotting.
  - `grid`: Toggles gridlines.
  - `plot`: Generates standard 2D x-y line plot.
  - `print`: Prints or exports plot to a file.
  - `title`: Sets top plot heading text.
  - `xlabel` / `ylabel`: Labels x-axis and y-axis.
  - `axes`: Generates axes objects.
  - `close`: Closes current figure window.
  - `close all`: Closes all open figures.
  - `figure`: Opens a fresh figure window.
  - `gtext`: Interactive text label placement using mouse.
  - `hold`: Retains current plot when adding new data.
  - `legend`: Adds legend box.
  - `refresh`: Redraws figure.
  - `set`: Sets object/axes properties.
  - `subplot`: Arranges multiple axes in subwindows.
  - `text`: Places text string at specified coordinates.
  - `bar`: Generates bar chart.
  - `loglog`: Dual logarithmic scale plot.
  - `polar`: Polar coordinates plot.
  - `semilogx` / `semilogy`: Logarithmic x-axis / y-axis plots.
  - `stairs`: Stair-step plot.
  - `stem`: Discrete stem/needle plot.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-44.png`
- **Slide Title**: To plot the graph of a function / To add titles, labels, grid lines and scaling on the graph
- **Key Facts & Commands**:
  - Graphing steps: define domain `x`, calculate `y = f(x)`, invoke `plot(x, y)`.
  - Annotation and scaling commands:
    - `xlabel('...')`, `ylabel('...')`, `title('...')`
    - `grid on`: draws background grid.
    - `axis equal`: enforces identical tick unit lengths on both axes.
    - `axis square`: renders the plot region as a square box.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-45.png`
- **Slide Title**: Customizing a Plot: Color, Line Types, Marker Types
- **Table Values (`LineSpec`)**:
  - **Colors**: `b` (blue), `c` (cyan), `g` (green), `k` (black), `m` (magenta), `r` (red), `w` (white), `y` (yellow).
  - **Markers**: `o` (circle), `d` (diamond), `h` (hexagram), `p` (pentagram), `+` (plus), `.` (point), `s` (square), `*` (star), `v` (down triangle), `<` (left triangle), `>` (right triangle), `^` (up triangle), `x` (x-mark).
  - **Line styles**: `--` (dashed), `-.` (dash dot), `:` (dotted), `-` (solid).

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-46.png`
- **Slide Title**: Scripts to Produce Plots (Example 1)
- **Code & Values**:
  ```matlab
  x=11;
  y=48;
  plot(x,y, 'r*')
  xlabel('Time')
  ylabel('Temperature');
  title('Time and Temp')
  ```
- **Key Facts**: Demonstrates plotting a single point at coordinates $(11, 48)$ using a red asterisk.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-47.png`
- **Slide Title**: Scripts to Produce Plots (Example 2)
- **Code & Values**:
  ```matlab
  x = 1:6;
  y=[1 5 3 9 11 8];
  plot(x,y)
  ```
- **Key Facts**: Plots connected line segments across points $(1,1), (2,5), (3,3), (4,9), (5,11), (6,8)$.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-48.png`
- **Slide Title**: Scripts to Produce Plots (Example 3)
- **Code & Values**:
  - Bar chart:
    ```matlab
    x = 1:5;
    y1 = [2 11 6 9 3];
    bar(x,y1)
    ```
  - Overlaid line & marker plot:
    ```matlab
    x = 1:5;
    plot(x,y1,'k')
    hold on
    plot(x,y1,'ko')
    grid on
    legend('y1','y2')
    ```
- **Key Facts**: Shows using `hold on` to overlay a black continuous line (`'k'`) and circle markers (`'ko'`) on the same dataset.

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-49.png`
- **Slide Title**: Scripts to Produce Plots (Examples 4 & 5)
- **Code & Values**:
  - Example 4 (Multi-curve plot):
    ```matlab
    x = [0: 0.01: 10];
    y = sin(x);
    g = cos(x);
    plot(x,y,x,g, '.-'), legend('Sin(x)', 'Cos(x)')
    ```
  - Example 5 (Bar chart):
    ```matlab
    x= [1:10];
    y=[75, 58, 90, 87, 50, 85, 92, 75, 60, 95];
    bar(x,y)
    xlabel('Student');
    ylabel('Score');
    title('First Sem:')
    ```

---

#### `img/M4-MAIN - Monte Carlo Simulation-page-50.png`
- **Slide Title**: Basics of MATLAB: Three Dimensional Plots
- **Key Facts & Functions**:
  - 3D function names typically append `3` to 2D equivalents: `plot3`, `bar3`, `bar3h`, `pie3`, `comet3`, `stem3`.
  - Vectors representing $(x, y, z)$ coordinates are passed directly into `plot3(x,y,z)` or `stem3(x,y,z)`.
  - `zlabel` adds a label to the z-axis.
  - Interactive figure tools include the 3D rotation tool and toggling `grid`.

---

### Possible slide errors

1. **Slide 35 (Page 35)**:
   - **Variable name mismatch in command window**: The prompt assigns to `mat2` (`>> mat2 = rand(3,3)`), but the response outputs `mymat =` instead of `mat2 =`.
2. **Slide 43 (Page 43)**:
   - **Misleading description of `legend`**: The purpose is given as `"Legend placement by mouse."` In MATLAB, `legend(...)` programmatically creates and labels legend entries (defaulting to the top right corner); it is not primarily a mouse-placement tool (unlike `gtext`).
3. **Slide 46 (Page 46)**:
   - **Spelling error**: The comment reads `plot a read '*'` instead of `plot a red '*'`.
   - **Missing executable axis statement**: The command `axis([9 12 34 55])` is trapped inside a comment line (`%change the axes and label them axis([9 12 34 55])`). If copied directly, the custom axis scaling would not execute. Furthermore, the y-range comment says `34 55`, while the plot display begins at `35`.
4. **Slide 48 (Page 48)**:
   - **Erroneous legend label**: In the second snippet, the code calls `legend('y1','y2')`, but the second plot call is simply `plot(x,y1,'ko')` (the same variable `y1` plotted with circles). Labeling the marker layer `'y2'` is incorrect because there is no `y2` data series.

### [img/M4-MAIN - Monte Carlo Simulation-page-51.png](file:///D:/School-Works/Modeling and Simulation/ModSim Exam Prep/sources/picture_notes/img/M4-MAIN - Monte Carlo Simulation-page-51.png)

* **Slide Title:** Basics of MATLAB – Three Dimensional Plots
* **Key Concepts & Commands:**
  * **3D Point/Line Plotting (`plot3`):** Generates three-dimensional line or point plots using $x$, $y$, and $z$ coordinate vectors. 
  * **Grid & Annotation:** `grid` activates grid lines across the 3D axes; standard labeling commands `xlabel()`, `ylabel()`, `zlabel()`, and `title()` annotate each dimension.
  * **3D Bar Graph (`bar3`):** Produces three-dimensional vertical bar charts.
* **Code & Data Shown:**
  * **Example 1 (3D Scatter/Line):**
    ```matlab
    x=1:5;
    y=[0 -2 4 11 3];
    z= 2:2:10;
    plot3(x,y,z, 'k*')
    grid
    xlabel('x')
    ylabel('y')
    zlabel('z')
    title('3D Plot')
    ```
    * Points plotted with black asterisks (`'k*'`) at coordinates: $(1, 0, 2)$, $(2, -2, 4)$, $(3, 4, 6)$, $(4, 11, 8)$, and $(5, 3, 10)$.
  * **Example 2 (3D Bar Chart):**
    ```matlab
    y = 1:6;
    x = 1:6;
    z= [ 33 11 5 9 22 30];
    bar3(y,z)
    xlabel('x')
    ylabel('y')
    zlabel('z')
    title('3D Bar')
    ```
    * Bar heights correspond to values: $33, 11, 5, 9, 22, 30$.

---

### [img/M4-MAIN - Monte Carlo Simulation-page-52.png](file:///D:/School-Works/Modeling and Simulation/ModSim Exam Prep/sources/picture_notes/img/M4-MAIN - Monte Carlo Simulation-page-52.png)

* **Slide Title:** Basics of MATLAB – Three Dimensional Plots
* **Key Concepts & Commands:**
  * **Matrix Visualization via `bar3`:** Passing a 2D matrix to `bar3` renders a 3D bar surface where row and column indices define the horizontal grid and matrix entries determine bar heights.
  * **Built-in `spiral(n)`:** Generates an $n \times n$ matrix containing integers from $1$ to $n^2$ winding spirally from the center.
  * **3D Pie Chart (`pie3`):** Renders proportions of an input vector in 3D slices with percentage callouts automatically calculated.
* **Code & Data Shown:**
  * **Example 3 (Matrix Bar Plot):**
    ```matlab
    mat = spiral(5)
    bar3(mat)
    title('3D Spiral');
    xlabel('x')
    ylabel('y')
    zlabel('z')
    ```
    * Generates a $5 \times 5$ matrix of values from $1$ to $25$ plotted across 5 rows and 5 columns.
  * **Example 4 (3D Pie Chart):**
    ```matlab
    >> pie3([3 10 5 2])
    ```
    * Values: $[3, 10, 5, 2]$ (Total sum = $20$).
    * Computed percentages:
      * $10 / 20 = 50\%$
      * $5 / 20 = 25\%$
      * $3 / 20 = 15\%$
      * $2 / 20 = 10\%$

---

### Possible slide errors

1. **Slide 51 (Dimension Mismatch in Example 2):** 
   * In MATLAB, calling `bar3(y, z)` requires the length of vector `y` to equal the number of rows in `z` (`length(y) == size(z, 1)`). Here, `y` has length $6$, but `z` is defined as a $1 \times 6$ row vector (`size(z, 1) = 1`). Running this exact code in MATLAB throws an error: `Error using bar3: Y must be a vector with length equal to the number of rows in Z.` To match the slide's output figure, `z` must be transposed (`bar3(y, z')` or `z = [33 11 5 9 22 30]'`).
2. **Slide 51 (Unused Variable in Example 2):**
   * The vector `x = 1:6;` is defined in the script but never passed to `bar3(y, z)` or any other function, making it redundant dead code.
3. **Slide 52 (Duplicate Title Header):**
   * The header "Three Dimensional Plots" is duplicated in red text directly above Example 4, awkwardly repeating the slide's main title.
4. **Slide 52 (Inconsistent Command Prompt Inclusion):**
   * Example 4 includes the interactive command prompt symbol (`>> pie3(...)`), whereas Examples 1, 2, and 3 are formatted as clean script blocks without prompt symbols.
