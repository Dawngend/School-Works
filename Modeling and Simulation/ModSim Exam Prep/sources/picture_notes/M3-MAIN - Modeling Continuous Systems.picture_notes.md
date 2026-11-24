### Study Notes: Module 3 – Modeling Continuous Systems

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-1.png`
* **Slide Title:** Modeling and Simulation
* **Key Facts & Information:** Course title slide featuring university institutional affiliations (FEU Alabang, FEU Diliman, FEU Tech) and the motto *"Technology Driven by Innovation"*.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-2.png`
* **Slide Title:** MODULE 3: MODELING CONTINUOUS SYSTEMS
* **Key Facts & Information:** Module title divider slide introducing continuous systems modeling.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-3.png`
* **Slide Title:** SUBTOPIC 1: CONTINUOUS SYSTEMS
* **Key Facts & Information:** Subtopic divider introducing continuous system concepts, frameworks, and equations.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-4.png`
* **Slide Title:** OBJECTIVES
* **Key Facts & Information:** 
  * Describe continuous systems frameworks.
  * Illustrate the mechanics of continuous systems modeling.
  * Identify numerical methods used to model continuous systems.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-5.png`
* **Slide Title:** Modeling Continuous Systems – What is a continuous system?
* **Key Facts & Information:**
  * Defines continuous systems where variables change continuously across continuous time.
  * Continuous signals are denoted as functions of continuous time using parentheses: $x(t)$, $y(t)$.
  * Block diagram representation:
    $$\text{Input } x(t) \longrightarrow \left[\text{Continuous System}\right] \longrightarrow \text{Output } y(t)$$

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-6.png`
* **Slide Title:** Modeling Continuous Systems – Another example:
* **Key Facts & Information:**
  * Models a continuous reservoir with infinite capacity where fluid is continuously accumulated:
    $$\text{contents} = \int \text{input} \, dt$$
  * State variable $q(t)$: current reservoir fluid contents.
  * Input $x(t)$: rate of change of volume (inflow if positive, outflow if negative).
  * State differential equation:
    $$\frac{dq(t)}{dt} = x(t)$$
  * Output equation:
    $$y(t) = q(t)$$
  * Block representation: input $x \longrightarrow \left[\int\right] \longrightarrow q$.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-7.png`
* **Slide Title:** Modeling Continuous Systems – Application Areas
* **Key Facts & Applications:**
  * **Civil Engineering:** Embankment dam design and tunnel construction.
  * **Military:** Missile trajectory computation, pilot/fighter aircraft flight training simulators, intelligent control for underwater vehicles.
  * **Logistics:** Toll plaza throughput planning, airport terminal passenger flow analysis, proactive flight scheduling.
  * **Business Development:** Product development roadmaps, staffing level planning, market dynamics analysis.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-8.png`
* **Slide Title:** Modeling Continuous Systems – System Class: Mathematical Classes of Continuous Systems
* **Key Facts & Table Values:**
  * *First-order ordinary differential equations:*
    * Applications: Predator–prey interactions.
    * Formulas: $\dot{x} = x f(x, y)$, $\dot{y} = y g(x, y)$
  * *Second-order ordinary differential equations:*
    * Applications: Orbits, oscillators, ballistics: $\mathbf{F} = m\mathbf{a}$
    * Applications: RLC circuits:
      $$L\ddot{q} + R\dot{q} + \frac{1}{C}q = V(t)$$
  * *Second-order partial differential equations:*
    * Applications: Waves, diffusion, heat transfer:
      $$\nabla^2 f = \frac{1}{D}\frac{\partial f}{\partial t} - \frac{1}{v^2}\frac{\partial^2 f}{\partial t^2}$$
    * Applications: Quantum mechanics (Schrödinger’s equation):
      $$i\hbar\frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\Psi + V\Psi$$
  * *Key Note:* The overwhelming majority of continuous engineering and physical models are governed by second-order differential equations.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-9.png`
* **Slide Title:** Modeling Continuous Systems – M&S Strategy: Modeling and Simulation Strategy
* **Key Facts & Strategy Flow:**
  1. Translate the physical real-world system into mathematical equations ("Physics").
  2. Implement numerical algorithms to compute solutions computationally.
  * Example: Orbital satellite motion: $\mathbf{F} = m\mathbf{a} \implies -\frac{GMm}{r^3}\mathbf{r} = m\mathbf{a}$.
  * Quoted MATLAB implementation snippet:
```matlab
options = odeset('RelTol',1.e-4);
[t,xvOut] = ode45(@(t,xv)
gravFunc(t,xv,m),[t0,t1],xv0,options);
function xvderiv = orbitfunc_complete(t,xv)
...
% derivative of position vector
xvderiv(1,1) = xv(4,1);
xvderiv(2,1) = xv(5,1);
xvderiv(3,1) = xv(6,1);

% derivative of velocity vector
xvderiv(4,1) = -GM*xv(1,1)/r^3;
xvderiv(5,1) = -GM*xv(2,1)/r^3;
xvderiv(6,1) = -GM*xv(3,1)/r^3;
```

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-10.png`
* **Slide Title:** Modeling Continuous Systems – Modeling Approach
* **Key Facts & Definitions:**
  * **State Variables:**
    * Continuous in time and continuous-valued (real or complex, not discrete integers).
    * Must form a minimal complete set capable of capturing all required physical dynamics.
    * Examples: position, velocity, mass, rate, angle, fraction, electric current, voltage.
  * **State Variable Equations:**
    * Governing differential equations specifying time derivatives of each state variable ($\dot{\mathbf{x}} = f(\mathbf{x}, t)$).

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-11.png`
* **Slide Title:** Modeling Continuous Systems – Modeling Approach
* **Key Facts & Formulas (Planetary Orbits):**
  * **Output Equations:** Algebraic equations converting internal state variables into user-requested outputs.
  * State vector contains 3D position $(x, y, z)$ and 3D velocity $(v_x, v_y, v_z)$.
  * Derived outputs:
    * Distance from origin: $r = \sqrt{x^2 + y^2 + z^2}$
    * Orbital speed: $v = \sqrt{v_x^2 + v_y^2 + v_z^2}$
    * Specific orbital energy:
      $$E = -\frac{GMm}{r} + \frac{1}{2}mv^2 = -\frac{GMm}{2a}$$
      *(where $G$ is the gravitational constant, $M$ is solar mass, $m$ is planetary mass, and $a$ is the semi-major axis)*.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-12.png`
* **Slide Title:** Modeling Continuous Systems – Model Examples: Predator-Prey Models
* **Key Facts & Concepts:**
  * Represents coupled dynamic populations of two interacting species whose birth and mortality rates depend mutually on each other's abundance.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-13.png`
* **Slide Title:** Modeling Continuous Systems – Model Examples
* **Key Facts & Feedback Loop:**
  * 9-stage population cycle:
    1. Prey population increases.
    2. Predators feast on plentiful prey.
    3. Predator population increases.
    4. Predators overhunt the prey population.
    5. Prey population drops.
    6. Predators starve.
    7. Predator population collapses.
    8. Surviving prey experience reduced predation pressure.
    9. Prey population thrives and rebounds (repeats to stage 1).

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-14.png`
* **Slide Title:** Modeling Continuous Systems – Model Examples
* **Key Facts & Formulas (Kolmogorov Formulation):**
  * General 2-species predator-prey system:
    $$\dot{x} = x f(x, y)$$
    $$\dot{y} = y g(x, y)$$
    where $x$ is prey population, $y$ is predator population.
  * Functions $f(x, y)$ and $g(x, y)$ denote per capita growth rates ($f = \frac{d}{dt}\ln x$).
  * Increased predator population $y$ decreases the per capita prey growth rate $f$ ($\frac{\partial f}{\partial y} < 0$).

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-15.png`
* **Slide Title:** Modeling Continuous Systems – Model Examples: Lotka-Volterra Model
* **Key Facts & Formulas:**
  * Specific linear per capita growth rate functions:
    $$f = b - py$$
    $$g = rx - d$$
  * Parameters: $b$ (natural prey birth rate), $p$ (predation rate per predator), $r$ (predator reproduction efficiency per prey consumed), $d$ (predator natural death rate).
  * $f$ is linear in $y$ with negative slope ($-p$); $g$ is linear in $x$ with positive slope ($+r$).

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-16.png`
* **Slide Title:** Modeling Continuous Systems – Model Examples
* **Key Facts & Formulas:**
  * Invariant quantity / conservation law satisfied along trajectories:
    $$C = b \ln y - py - x + d \ln x$$
  * The constant $C$ remains constant in time for any trajectory $(x(t), y(t))$ and is fixed by initial conditions $(x(0), y(0))$.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-17.png`
* **Slide Title:** Modeling Continuous Systems – Model Examples
* **Key Facts & Phase Portrait:**
  * Shows phase plane orbits (level curves of $C$) for $r = b = d = p = 1$.
  * Horizontal axis: Prey $x \in [0, 4]$; Vertical axis: Predator $y \in [0, 4]$.
  * Exhibits closed concentric periodic cycles orbiting around the equilibrium point $(1, 1)$.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-18.png`
* **Slide Title:** Simulating Continuous Systems: Numerical Solution Techniques
* **Key Facts & Formulas:**
  * Numerical integration is necessary because most nonlinear differential equations lack closed-form analytical solutions.
  * **Euler’s Forward Method:**
    $$\frac{dx}{dt} \approx \frac{x(t + \Delta t) - x(t)}{\Delta t}$$
    $$x(t + \Delta t) \approx x(t) + \left.\frac{dx}{dt}\right|_{x, t}\Delta t$$
    $$x(t + \Delta t) \approx x(t) + f(x, t)\Delta t$$

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-19.png`
* **Slide Title:** Simulating Continuous Systems: 2. Runge-Kutta Method
* **Key Facts & Formulas (Explicit Midpoint / RK2 Formulation):**
  * Half-step time:
    $$t_{1/2} = t_0 + \frac{\Delta t}{2}$$
  * Midpoint prediction:
    $$x_{1/2} = x_0 + f(t_0, x_0)\frac{\Delta t}{2}$$
  * Step update using midpoint slope:
    $$x_1 = x_0 + f(t_{1/2}, x_{1/2})\Delta t$$

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-20.png`
* **Slide Title:** Formative Assessment 4
* **Key Facts & Information:** Directs students to check Canvas for formative assessment instructions.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-21.png`
* **Slide Title:** Summative Assessment 3
* **Key Facts & Information:** Directs students to check Canvas for summative assessment instructions.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-22.png`
* **Slide Title:** References
* **Key Sources:**
  * JavaTpoint continuous vs. discrete systems tutorial.
  * SlidePlayer presentation 5735712.
  * TutorialsPoint continuous simulation resources.
  * Textbook: Sokolowski, J. A., & Banks, C. M. (2010). *Modeling and Simulation Fundamentals: Theoretical Underpinnings and Practical Domains*. John Wiley & Sons.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-23.png`
* **Slide Title:** MATLAB Programming Basics (Modeling and Simulation)
* **Key Facts & Information:** Section divider introducing MATLAB computational workflows.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-24.png`
* **Slide Title:** Subtopic 2: MATLAB Progaming: MATLAB Programming Basics (Input, Output, & Decision Statement)
* **Key Facts & Information:** Subtopic introduction covering MATLAB I/O and branching logic.

---

#### `img/M3-MAIN - Modeling Continuous Systems-page-25.png`
* **Slide Title:** OBJECTIVES
* **Key Learning Goals:**
  * Construct MATLAB scripts.
  * Create single-value user-defined functions.
  * Use fundamental MATLAB input and output commands.
  * Implement conditional selection statements and loops in MATLAB scripts.

---

### Possible Slide Errors

1. **Slide 5 — Inaccurate/Contradictory Definition of Continuous Systems:**
   * *Issue:* The slide states that continuous systems are *"those types of systems in which input and output signals are the same at both the ends"* and that *"any type of variation is not found in the input and output signal."*
   * *Why it is wrong:* A continuous system is defined by its state and signals varying smoothly over a continuum of time ($t \in \mathbb{R}$), not by input and output signals being identical or unvarying. In fact, inputs and outputs commonly differ and vary continuously over time.

2. **Slide 8 — Conflated Partial Differential Equation:**
   * *Issue:* The formula listed for water/sound waves and heat/chemical diffusion is:
     $$\nabla^2 f = \frac{1}{D}\frac{\partial f}{\partial t} - \frac{1}{v^2}\frac{\partial^2 f}{\partial t^2}$$
   * *Why it is wrong:* This incorrectly combines the parabolic diffusion equation ($\nabla^2 f = \frac{1}{D}\frac{\partial f}{\partial t}$) and the hyperbolic wave equation ($\nabla^2 f = \frac{1}{v^2}\frac{\partial^2 f}{\partial t^2}$) into a single hybrid expression. Classical diffusion has no second-order time derivative, and lossless wave propagation has no first-order time dissipation term.

3. **Slide 9 — Mismatched Function Name in MATLAB Code:**
   * *Issue:* The call to the solver invokes `ode45(@(t, xv) gravFunc(t, xv, m), ...)`, while the helper function defined immediately below is named `function xvderiv = orbitfunc_complete(t, xv)`.
   * *Why it is wrong:* Unless an external `gravFunc` file exists, calling `ode45` with `@gravFunc` will result in an "unrecognized function or variable" error in MATLAB because the definition uses `orbitfunc_complete`.

4. **Slide 16 — Missing Parameter in the Conservation Law:**
   * *Issue:* The conservation formula is written as:
     $$C = b \ln y - py - x + d \ln x$$
   * *Why it is wrong:* Integrating the general Lotka-Volterra system with $g(x) = rx - d$ yields $C = b \ln y - py - rx + d \ln x$. The coefficient $r$ was omitted before $x$, which is only valid if $r = 1$ is assumed beforehand.

5. **Slide 19 — Ambiguous Naming for Runge-Kutta:**
   * *Issue:* The slide titles the method generically as "Runge-Kutta Method" while only presenting the explicit midpoint method (2nd-order Runge-Kutta, RK2).
   * *Why it is misleading:* In standard modeling and simulation literature, "the Runge-Kutta Method" without qualification typically refers to the classical 4th-order scheme (RK4).

6. **Slide 24 — Typographical Error in Title:**
   * *Issue:* The slide heading contains `"MATLAB Progaming"`.
   * *Why it is wrong:* Spelling error; the correct spelling is `"Programming"`.

7. **Slide 25 — Grammatical Agreement Error:**
   * *Issue:* Bullet 2 reads: *"Create user-defined functions that returns a single value."*
   * *Why it is wrong:* Plural subject `"functions"` requires the plural verb `"return"`.

### Study Notes: Modeling Continuous Systems (Slides 26–50)

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-26.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-26.png)
- **Slide Title:** Input and Output
- **Key Facts:** Section transition slide introducing MATLAB input and output mechanisms.

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-27.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-27.png)
- **Slide Title:** Toolstrip and Editor
- **Key Facts:**
  - Shows MATLAB desktop interface layout: Toolstrip (tabs for Home, Plots, Apps, Shortcuts) and Editor window (`Editor - untitled`).
  - Home tab groups: File (`New Script`, `New`, `Open`, `Find Files`, `Compare`), Variable (`Import Data`, `Save Workspace`, `New Variable`, `Open Variable`, `Clear Workspace`), Code (`Analyze Code`, `Run and Time`, `Clear Commands`), Environment (`Layout`, `Preferences`, `Set Path`).
  - Editor tab contains controls: `Breakpoints`, `Run`, `Run and Time`, `Run and Advance`, `Run Section`, `Advance`.
  - Scripts are saved with the `.m` extension (`<filename>.m`).

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-28.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-28.png)
- **Slide Title:** [MATLAB Online Environment / Workspace Overview]
- **Key Facts & Values:**
  - Displays the MATLAB Drive / MATLAB Online interface (`matlab.mathworks.com`).
  - **Current Folder contents:** `untitled4.m`, `untitled3.m`, `untitled3.asv`, `untitled1.slx.autosave`, `untitled.slx.autosave`, `textdata.out`, `testfile.day`, `testfile.dat`, `test.mat`, `scope1.slx.autosave`, `scope1.slx`, `sample.mat`.
  - **Workspace variables displayed:**
    - `a`: `'Stateflow'` (1×1 string)
    - `ans`: `[20, 19, 20, 19, 16]` (1×5 double)
    - `b`: `[7, 9, 11]` (1×3 double)
    - `c`: `3` (1×1 double)
    - `evec`: `[4, 11, 121]` (1×3 double)
    - `mat`: 3×5 double

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-29.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-29.png)
- **Slide Title:** The M Files
- **Key Facts:**
  - MATLAB provides two kinds of program files:
    - **Scripts:** Program files with `.m` extension containing sequential commands executed together; do not take formal arguments or return outputs; directly access and manipulate base workspace variables.
    - **Functions:** Program files with `.m` extension; accept input arguments and return outputs; internal variables reside in private local scopes.
  - **Code shown:**
    ```matlab
    r = input('Enter the radius: ')
    A = pi * (r^2)
    ```

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-30.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-30.png)
- **Slide Title:** MATLAB Programming Basics – Creating and Running Script File
- **Key Facts:**
  - Text editors are used to create MATLAB script files.
  - Editor can be opened either via IDE GUI buttons or command prompt.
  - Command syntax:
    ```matlab
    edit
    % Or
    edit <filename>
    ```

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-31.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-31.png)
- **Slide Title:** MATLAB Programming Basics – Creating Directory for Saving Scripts
- **Key Facts & Code:**
  - Directory creation and navigation commands:
    ```matlab
    mkdir progs      % create directory progs under default directory
    chdir progs      % changing the current directory to progs
    edit  prog1.m    % creating an m file named prog1.m
    ```

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-32.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-32.png)
- **Slide Title:** Example of Scripts
- **Key Facts, Code & Formulas:**
  - File `script1.m`:
    ```matlab
    radius = 5
    area = pi * (radius^2)
    ```
  - Inspecting with `type`: `>> type script1` prints file code.
  - Running script:
    ```matlab
    >> script1
    radius =
         5
    area =
       78.5398
    ```
  - **Geometric Area Formulas Table:**
    - Area of Rectangle: $\text{Area} = l \times w$ ($l = \text{length}, w = \text{width}$)
    - Area of Square: $\text{Area} = a^2$ ($a = \text{side length}$)
    - Area of a Triangle: $\text{Area} = 1/2 \, b \times h$ ($b = \text{base}, h = \text{height}$)
    - Area of a Circle: $\text{Area} = \pi r^2$ ($r = \text{radius}$)

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-33.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-33.png)
- **Slide Title:** Examples of script
- **Key Facts & Code:**
  - String array addition (element-wise concatenation):
    ```matlab
    s1 = ["Red" "Blue" "Green"]
    s2 = ["Truck" "Sky" "Tree"]
    s = s1 + s2
    ```
  - Implicit expansion / vector addition:
    ```matlab
    a = 1:2;
    b = (1:3)';
    a + b
    ```
  - Matrix addition:
    ```matlab
    A = [1 0; 2 4];
    B = [5 9; 2 1];
    C = A + B
    ```

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-34.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-34.png)
- **Slide Title:** Examples of Using Input Commands (script)
- **Key Facts, Code & Values:**
  - Prompting for numeric input:
    ```matlab
    input("Enter an integer : ")
    % Output: Enter an integer : 10 -> ans = 10
    ```
  - Prompting for string/character input with `'s'` flag:
    ```matlab
    input("Enter a string : ", "s")
    % Output: Enter a string : FEU_Tech -> ans = FEU_Tech
    ```
  - Multi-input script performing arithmetic:
    ```matlab
    x = input("Enter a number")
    y = input("Enter another number")
    z1 = x + y
    z2 = x - y
    z3 = x * y
    z4 = (x + y)/2
    ```

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-35.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-35.png)
- **Slide Title:** [Formatted Output with Script]
- **Key Facts & Code:**
  - Continuation of arithmetic script using `fprintf` formatted displays:
    ```matlab
    x = input("Enter a number ")
    y = input("Enter another number ")
    z1 = x + y
    z2 = x - y
    z3 = x * y
    z4 = (x + y)/2
    fprintf('\n Sum is. %d ',z1);
    fprintf('\n Difference is. %d',z2);
    fprintf('\n Product is. %d',z3);
    fprintf('\n Average is. %d',z4);
    ```

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-36.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-36.png)
- **Slide Title:** [Display Functions: disp vs fprintf]
- **Key Facts & Code:**
  - `disp(X)` prints array or text values without printing variable names; typing a variable alone adds the `X =` header.
  - Code examples:
    ```matlab
    A = [15 150];
    disp(A)

    S = 'Hello World.';
    disp(S)

    disp('Corn    Oats    Hay')

    X = rand(5,3);
    disp(X)

    X = '<a href = "https://www.mathworks.com">MathWorks Web Site</a>';
    disp(X)
    ```
  - `fprintf` formats output directly to screen without creating variables; requires `\n` to end line.
    ```matlab
    name = 'Alice';
    age = 12;
    fprintf('%s will be %d this year.\n',name,age);
    ```

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-37.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-37.png)
- **Slide Title:** Input and Output Commands
- **Key Facts & Table Values:**
  | Command | Purpose |
  | :--- | :--- |
  | `disp` | Displays contents of an array or string. |
  | `fscanf` | Read formatted data from a file. |
  | `format` | Controls screen-display format. |
  | `fprintf` | Performs formatted writes to screen or file. |
  | `input` | Displays prompts and waits for input. |
  | `;` | Suppresses screen printing. |

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-38.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-38.png)
- **Slide Title:** Input and Output Commands
- **Key Facts & Format Codes:**
  - `fscanf` and `fprintf` follow C library formatting conventions.
  | Format Code | Purpose |
  | :--- | :--- |
  | `%s` | Format as a string. |
  | `%d` | Format as an integer. |
  | `%f` | Format as a floating point value. |
  | `%e` | Format as a floating point value in scientific notation. |
  | `%g` | Format in the most compact form: `%f` or `%e`. |
  | `\n` | Insert a new line in the output string. |
  | `\t` | Insert a tab in the output string. |

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-39.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-39.png)
- **Slide Title:** MATLAB Programming Basics – Input and Output Commands
- **Key Facts & Table Values (`format` forms):**
  | Format Function | Display Up To |
  | :--- | :--- |
  | `format short` | Four decimal digits (default). |
  | `format long` | 16 decimal digits. |
  | `format short e` | Five digits plus exponent. |
  | `format long e` | 16 digits plus exponents. |
  | `format bank` | Two decimal digits. |
  | `format +` | Positive, negative, or zero. |
  | `format rat` | Rational approximation. |
  | `format compact`| Suppresses some line feeds. |
  | `format loose` | Resets to less compact display mode. |

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-40.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-40.png)
- **Slide Title:** MATLAB Programming Basics – Examples of Using Input Commands Interactively
- **Key Facts & Code:**
  - Standard prompt:
    ```matlab
    >> rad = input('Enter the radius: ')
    Enter the radius: 5
    rad =
         5
    ```
  - Multiline prompt via `\n`:
    ```matlab
    >> x = input('Enter the \nx coordinate: ');
    Enter the 
    x coordinate: 4
    ```
  - Using `'s'` argument:
    ```matlab
    >> letter = input('Enter a char: ','s')   % input 'g' -> letter = 'g'
    >> mychar = input('Enter a character: ', 's') % pressing Enter produces empty char ''
    >> mystr = input('Enter a string: ', 's')  % input '    go' (4 spaces + 'go') -> length(mystr) is 6
    ```

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-41.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-41.png)
- **Slide Title:** Examples of Using Output Commands Interactively
- **Key Facts & Code:**
  - Simple displays:
    ```matlab
    >> disp('Hello')
    >> disp(4^3) % prints 64
    ```
  - Formatted `fprintf`:
    ```matlab
    >> fprintf('The value is %d, for sure!\n',4^3)
    The value is 64, for sure!

    >> fprintf('The int is %d and the char is %c\n', ...
        33 - 2, 'x')
    The int is 31 and the char is x

    >> fprintf('The int is %3d and the float is %6.2f\n', 5, 4.9)
    The int is   5 and the float is   4.90
    ```

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-42.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-42.png)
- **Slide Title:** Printing Vectors and Matrices Interactively
- **Key Facts & Code:**
  - When `fprintf` prints vectors and matrices, it processes elements in **column-major order**.
  - Vector examples:
    ```matlab
    >> vec = 2:5;
    >> fprintf('%d\n', vec)   % prints 2, 3, 4, 5 each on new line
    >> fprintf('%d', vec)     % prints 2345>> (without newline)
    >> fprintf('%d %d %d %d\n', vec) % prints 2 3 4 5
    ```
  - Matrix examples (`mat = [5 9 8; 4 1 10]`):
    ```matlab
    >> fprintf('%d\n', mat)
    % Prints column 1 then column 2 then column 3: 5, 4, 9, 1, 8, 10
    >> fprintf('%d %d %d\n', mat)
    % Consumes elements in groups of 3 down columns:
    % 5 4 9
    % 1 8 10
    ```

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-43.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-43.png)
- **Slide Title:** MATLAB Programming Basics – Vector, Matrix and Array Commands
- **Key Facts & Table Values:**
  | Command | Purpose |
  | :--- | :--- |
  | `cat` | Concatenates arrays. |
  | `find` | Finds indices of nonzero elements. |
  | `length` | Computes number of elements. |
  | `linspace` | Creates regularly spaced vector. |
  | `logspace` | Creates logarithmically spaced vector. |
  | `max` | Returns largest element. |
  | `min` | Returns smallest element. |
  | `prod` | Product of each column. |
  | `reshape` | Changes size. |
  | `size` | Computes array size. |
  | `sort` | Sorts each column. |

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-44.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-44.png)
- **Slide Title:** MATLAB Programming Basics – Vector, Matrix and Array Commands
- **Key Facts & Table Values:**
  | Command | Purpose | Command | Purpose |
  | :--- | :--- | :--- | :--- |
  | `sum` | Sums each column. | `celldisp` | Displays cell array. |
  | `eye` | Creates an identity matrix. | `cellplot` | Displays graphical representation of cell array. |
  | `ones` | Creates an array of ones. | `num2cell` | Converts numeric array to cell array. |
  | `zeros` | Creates an array of zeros. | `deal` | Matches input and output lists. |
  | `cross` | Computes matrix cross products. | `iscell` | Identifies cell array. |
  | `dot` | Computes matrix dot products. | | |
  | `det` | Computes determinant of an array. | | |
  | `inv` | Computes inverse of a matrix. | | |
  | `pinv` | Computes pseudoinverse of a matrix. | | |
  | `rank` | Computes rank of a matrix. | | |
  | `rref` | Computes reduced row echelon form. | | |
  | `cell` | Creates cell array. | | |

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-45.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-45.png)
- **Slide Title:** MATLAB Programming Basics – Scripts with Input and Output
- **Key Facts & Code:**
  - Script `circleIO.m`:
    ```matlab
    % This script calculates the area of a circle
    % It prompts the user for the radius
    % Prompt the user for the radius and calculate
    % the area based on that radius
    fprintf('Note: the units will be inches.\n')
    radius = input('Please enter the radius: ');
    area = pi * (radius^2);
    % Print all variables in a sentence format
    fprintf('For a circle with a radius of %.2f inches,\n', radius)
    fprintf('the area is %.2f inches squared\n',area)
    ```
  - Execution output:
    ```matlab
    >> circleIO
    Note: the units will be inches.
    Please enter the radius: 3.9
    For a circle with a radius of 3.90 inches,
    the area is 47.78 inches squared
    ```

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-46.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-46.png)
- **Slide Title:** MATLAB Programming Basics – Plotting Commands
- **Key Facts & Table Values:**
  | Command | Purpose | Command | Purpose |
  | :--- | :--- | :--- | :--- |
  | `axis` | Sets axis limits. | `hold` | Freezes current plot. |
  | `fplot` | Intelligent plotting of functions. | `legend` | Legend placement by mouse. |
  | `grid` | Displays gridlines. | `refresh` | Redraws current figure window. |
  | `plot` | Generates xy plot. | `set` | Specifies properties of objects such as axes. |
  | `print` | Prints plot or saves plot to a file. | `subplot` | Creates plots in subwindows. |
  | `title` | Puts text at top of plot. | `text` | Places string in figure. |
  | `xlabel` | Adds text label to x-axis. | `bar` | Creates bar chart. |
  | `ylabel` | Adds text label to y-axis. | `loglog` | Creates log-log plot. |
  | `axes` | Creates axes objects. | `polar` | Creates polar plot. |
  | `close` | Closes the current plot. | `semilogx` | Creates semilog plot (logarithmic abscissa). |
  | `close all` | Closes all plots. | `semilogy` | Creates semilog plot (logarithmic ordinate). |
  | `figure` | Opens a new figure window. | `stairs` | Creates stairs plot. |
  | `gtext` | Enables label placement by mouse. | `stem` | Creates stem plot. |

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-47.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-47.png)
- **Slide Title:** MATLAB Programming Basics – To plot the graph of a function / To add titles, labels, grid lines and scaling on the graph
- **Key Facts:**
  - Steps to plot a graph:
    1. Define `x` range.
    2. Define function `y = f(x)`.
    3. Execute `plot(x, y)`.
  - Annotation and scaling commands:
    - `xlabel` and `ylabel`: Axis labels.
    - `title`: Plot title.
    - `grid on`: Display grid lines.
    - `axis equal`: Equal scale factors and unit lengths on both axes.
    - `axis square`: Produces square plot window.

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-48.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-48.png)
- **Slide Title:** MATLAB Programming Basics – Customizing a Plot: Color, Line Types, Marker Types
- **Key Facts & Specifiers:**
  - `LineSpec` allows up to 3 properties (color, marker symbol, line type) passed as a single string.
  - **Colors:** `b` (blue), `c` (cyan), `g` (green), `k` (black), `m` (magenta), `r` (red), `w` (white), `y` (yellow).
  - **Markers:** `o` (circle), `d` (diamond), `h` (hexagram), `p` (pentagram), `+` (plus), `.` (point), `s` (square), `*` (star), `v` (down triangle), `<` (left triangle), `>` (right triangle), `^` (up triangle), `x` (x-mark).
  - **Line Types:** `--` (dashed), `-.` (dash dot), `:` (dotted), `-` (solid).

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-49.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-49.png)
- **Slide Title:** MATLAB Programming Basics – Scripts to Produce Plots (Example 1)
- **Key Facts, Code & Values:**
  - Script `plotonepoint.m`:
    ```matlab
    % This is a really simple plot of just one point!
    % Create axis([x-2 x+2 y-10 y+10]) plot a red '*'
    x = 11;
    y = 48;
    plot(x,y,'r*')

    % Change the axes and label them axis([9 12 35 55])
    xlabel('Time')
    ylabel('Temperature')

    % Put a title on the plot
    title('Time and Temp')
    ```
  - Target plot shows single red star at coordinate `(11, 48)` on axes bounded $x \in [9, 12]$ and $y \in [35, 55]$.

---

#### [img/M3-MAIN - Modeling Continuous Systems-page-50.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-50.png)
- **Slide Title:** MATLAB Programming Basics – Scripts to Produce Plots (Example 2)
- **Key Facts & Code:**
  ```matlab
  >> x = 1:6;
  >> y = [1 5 3 9 11 8];
  >> plot(x,y)
  ```
  - Generates a continuous 2D line plot connecting $(1,1) \to (2,5) \to (3,3) \to (4,9) \to (5,11) \to (6,8)$.

---

### Possible Slide Errors

1. **Slide 28:**
   - **Error:** Missing a slide title and contextual labels. It presents uncaptioned raw screenshots of the MATLAB Online interface and workspace.

2. **Slide 29:**
   - **Error:** Contradiction between text and screenshot. The slide explicitly discusses standard MATLAB `.m` files, yet the embedded screenshot shows a file being saved as `untitled.mlx` (a MATLAB Live Script, which uses a different proprietary format).

3. **Slide 31:**
   - **Error:** Inconsistent filename. The command box executes `edit prog1.m`, but the editor screenshot immediately underneath shows a tab titled `prog2.m`.

4. **Slide 32:**
   - **Error:** Grammatical error in the area table. The variable column for Area of Square states `a = sides of the square` (plural); it should state "side" or "side length".

5. **Slide 35:**
   - **Error 1 (Title header):** The slide header erroneously repeats the bullet definition of "Functions" from Slide 29 (`•Functions –functions files are also program files with .m extension...`) instead of an appropriate title describing script output formatting.
   - **Error 2 (Formatting mismatch):** The script computes average with `z4 = (x + y)/2` and formats it using `fprintf('... %d', z4)`. `%d` is an integer specifier, meaning non-integer averages (e.g., $(3+4)/2 = 3.5$) will be formatted incorrectly or truncated instead of using a floating-point specifier like `%f` or `%.2f`.

6. **Slide 36:**
   - **Error:** Missing slide title banner. The slide begins immediately with raw explanatory text (`disp(X) displays the value...`).

7. **Slide 39:**
   - **Error:** Typo in table description. The description for `format long e` reads "16 digits plus exponents" (plural), whereas `format short e` correctly uses singular "exponent".

8. **Slide 44:**
   - **Error:** Imprecise mathematical descriptions:
     - `cross` is described as computing "matrix cross products", but in MATLAB `cross` computes the vector cross product of two 3-element vectors along a specified dimension.
     - `dot` is described as computing "matrix dot products", but it computes scalar dot products of vectors.
     - `det` is described as computing the determinant of an "array", whereas determinants are strictly defined only for square matrices (2D).

9. **Slide 46:**
   - **Error:** Inaccurate command description for `legend`. The purpose says "Legend placement by mouse", which misrepresents `legend`. By default, `legend` places legends based on strings and automatic location parameters; mouse placement applies to `gtext`, whereas mouse placement in `legend` was deprecated/specialized (`legend('toggle')` or dragging in GUI).

10. **Slide 49:**
    - **Error:** Missing executable command in the code snippet. The script comments mention `% Change the axes and label them axis([9 12 35 55])`, but the actual command `axis([9 12 35 55])` was omitted from execution. Without executing `axis([9 12 35 55])`, MATLAB would not have produced the explicit axis bounds $[9, 12]$ and $[35, 55]$ displayed in the accompanying figure.

Here are the study notes for the specified slides:

---

### [M3-MAIN - Modeling Continuous Systems-page-51.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-51.png)
- **Slide Title:** MATLAB Programming Basics / Scripts to Produce Plots (Example 3)
- **Key Concepts & Code:**
  - Demonstrates displaying multiple separate plots using different figure windows via `figure(n)` and clear figure with `clf`.
  - Script `plot2figs.m`:
    ```matlab
    clf
    x = 1:5; % Not necessary
    y1 = [2 11 6 9 3];
    y2 = [4 5 8 6 2];
    % Put a bar chart in Figure 1
    figure(1)
    bar(x,y1)
    % Put plots using different y values on one plot with a legend
    figure(2)
    plot(x,y1,'k')
    hold on
    plot(x,y2,'ko')
    grid on
    legend('y1','y2')
    ```
  - `bar(x, y1)` creates a vertical bar graph.
  - `figure(2)` overlays a black solid line (`'k'`) and black circle markers (`'ko'`) using `hold on`, with grid enabled via `grid on`.

---

### [M3-MAIN - Modeling Continuous Systems-page-52.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-52.png)
- **Slide Title:** MATLAB Programming Basics / Scripts to Produce Plots (Example 4)
- **Key Concepts & Code:**
  - Script `sinncos.m` plots $\sin(x)$ and $\cos(x)$ over $x \in [0, 2\pi]$ in steps of $2\pi/40$:
    ```matlab
    clf
    x = 0: 2*pi/40: 2*pi;
    y = sin(x);
    plot(x,y,'ro')
    hold on
    y = cos(x);
    plot(x,y,'b+')
    legend('sin', 'cos')
    xlabel('x')
    ylabel('sin(x) or cos(x)')
    title('sin and cos on one graph')
    ```
  - Note: Multiple plots can be combined into one call without `hold on`:
    `plot(x,sin(x),'ro',x,cos(x),'b+')`

---

### [M3-MAIN - Modeling Continuous Systems-page-53.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-53.png)
- **Slide Title:** MATLAB Programming Basics / Scripts to Produce Plots (Example 5)
- **Key Concepts & Code:**
  - Plots continuous sine and cosine curves over $x \in [0, 10]$ with step size $0.01$:
    ```matlab
    x = [0 : 0.01: 10];
    y = sin(x);
    g = cos(x);
    plot(x, y, x, g, '.-'), legend('Sin(x)', 'Cos(x)')
    ```
  - Uses compound format string `.-` (point markers connected by a solid line) for the second dataset.

---

### [M3-MAIN - Modeling Continuous Systems-page-54.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-54.png)
- **Slide Title:** MATLAB Programming Basics / Scripts to Produce Plots (Example 6)
- **Key Concepts & Code:**
  - Functions plotted:
    - $y = e^{-1.5x}\sin(10x)$
    - $y = e^{-2x}\sin(10x)$
  - Uses `subplot(rows, cols, index)` to tile plots side-by-side:
    ```matlab
    x = [0:0.01:5];
    y = exp(-1.5*x).*sin(10*x);
    subplot(1,2,1)
    plot(x,y), xlabel('x'),ylabel('exp(-1.5x)*sin(10x)'),axis([0 5 -1 1])
    y = exp(-2*x).*sin(10*x);
    subplot(1,2,2)
    plot(x,y),xlabel('x'),ylabel('exp(-2x)*sin(10x)'),axis([0 5 -1 1])
    ```
  - Requires element-wise multiplication `.*` between the exponential and sine vectors.
  - `axis([xmin xmax ymin ymax])` sets limits to $[0, 5, -1, 1]$.

---

### [M3-MAIN - Modeling Continuous Systems-page-55.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-55.png)
- **Slide Title:** MATLAB Programming Basics / MATLAB Simple Program
- **Key Concepts:**
  - General architecture between a script and a user-defined function:
    - `script.m`: Gets input $\rightarrow$ calls function `fn` passing arguments $\rightarrow$ receives output $\rightarrow$ prints result.
    - `fn.m`:
      ```matlab
      function out = fn(in)
      out = value based on in
      end
      ```

---

### [M3-MAIN - Modeling Continuous Systems-page-56.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-56.png)
- **Slide Title:** MATLAB Programming Basics / User Defined Functions
- **Key Concepts & Code:**
  - User-defined functions are stored in M-files (`.m`), named identically to the function itself.
  - General syntax:
    ```matlab
    function outputargument = functionname(input arguments)
    % Comment describing the function
    Statements here; these must include putting a value in the output argument
    end % of the function
    ```

---

### [M3-MAIN - Modeling Continuous Systems-page-57.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-57.png)
- **Slide Title:** MATLAB Programming Basics / User Defined Functions (Example 1)
- **Key Concepts & Code:**
  - Function definition (`calcarea.m`):
    ```matlab
    function area = calcarea(rad)
    % calcarea calculates the area of a circle
    % Format of call: calcarea(radius)
    % Returns the area
    area = pi * rad * rad;
    end
    ```
  - Calling script (`circleCallFn.m`):
    ```matlab
    radius = input('Please enter the radius: ');
    area = calcarea(radius);
    fprintf('For a circle with a radius of %.2f,', radius)
    fprintf(' the area is %.2f\n', area)
    ```
  - Sample output: For radius $5$, area is $78.54$.

---

### [M3-MAIN - Modeling Continuous Systems-page-58.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-58.png)
- **Slide Title:** MATLAB Programming Basics / User Defined Functions (Example 2)
- **Key Concepts & Code:**
  - Cone volume function (`conevol.m`):
    $$\text{Volume} = \frac{\pi}{3} r^2 h$$
    ```matlab
    function outarg = conevol(radius, height)
    % conevol calculates the volume of a cone
    % Format of call: conevol(radius, height)
    % Returns the volume
    outarg = (pi/3) * radius .^ 2 .* height;
    end
    ```
  - Terminal calls and results:
    - `conevol(4, 6.1)` $\rightarrow$ `ans = 102.2065`
    - `fprintf('The cone volume is %.2f\n', conevol(3, 5.5))` $\rightarrow$ `The cone volume is 51.84`

---

### [M3-MAIN - Modeling Continuous Systems-page-59.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-59.png)
- **Slide Title:** Selection and Looping
- **Key Concepts:**
  - Topic transition divider slide introducing conditional control flow and iterative structures in MATLAB.

---

### [M3-MAIN - Modeling Continuous Systems-page-60.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-60.png)
- **Slide Title:** Selection and Looping Statements / The IF Statement
- **Key Concepts & Code:**
  - Syntax forms:
    - Single-branch: `if condition` $\rightarrow$ `action` $\rightarrow$ `end`
    - Two-branch: `if condition` $\rightarrow$ `action1` $\rightarrow$ `else` $\rightarrow$ `action2` $\rightarrow$ `end`
  - Example execution:
    ```matlab
    a = 100;
    if a < 20
        fprintf('a is less than 20\n' );
    else
        fprintf('a is not less than 20\n' );
    end
    fprintf('value of a is : %d\n', a);
    ```
  - Output:
    ```text
    a is not less than 20
    value of a is : 100
    ```

---

### [M3-MAIN - Modeling Continuous Systems-page-61.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-61.png)
- **Slide Title:** Determine if the data is negative or positive / Odd or even number
- **Key Concepts & Code:**
  - Positive/Negative check:
    ```matlab
    x = input("Enter a number ");
    if x < 0
        fprintf('Negative');
    else
        fprintf('Positive');
    end
    ```
  - Odd/Even check using modulo remainder:
    ```matlab
    y = x % 2; % Note: MATLAB native is mod(x,2) or rem(x,2)
    if y == 0
        fprintf('Even number');
    else
        fprintf('Even number'); % Bug on slide
    end
    ```

---

### [M3-MAIN - Modeling Continuous Systems-page-62.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-62.png)
- **Slide Title:** Age problem
- **Key Concepts & Code:**
  - Multi-branch conditional grading of age using `elseif` and logical AND (`&&`):
    ```matlab
    age = input("Enter a age ");
    if age > 0 && age <= 13
        fprintf('young \n ');
    elseif age > 13 && age < 20
        fprintf('teen \n ');
    elseif age > 20 && age < 60
        fprintf('adult \n ');
    elseif age <= 100
        fprintf('senior \n ');
    else
        fprintf('sorry \n ');
    end
    fprintf("Thanks, keep safe");
    ```

---

### [M3-MAIN - Modeling Continuous Systems-page-63.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-63.png)
- **Slide Title:** Selection and Looping Statements / The Switch Statement
- **Key Concepts & Code:**
  - General syntax:
    ```matlab
    switch switch_expression
        case caseexp1
            action1
        case caseexp2
            action2
        otherwise
            actionn
    end
    ```
  - Example using letter grade:
    ```matlab
    grade = 'B';
    switch(grade)
        case 'A'
            fprintf('Excellent!\n' );
        case 'B'
            fprintf('Well done\n' );
        case 'C'
            fprintf('Well done\n' );
        case 'D'
            fprintf('You passed\n' );
        case 'F'
            fprintf('Better try again\n' );
        otherwise
            fprintf('Invalid grade\n' );
    end
    ```

---

### [M3-MAIN - Modeling Continuous Systems-page-64.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-64.png)
- **Slide Title:** Selection and Looping Statements (Switch Statement Examples)
- **Key Concepts & Code:**
  - Left column repeats the letter grade switch example.
  - Right column evaluates relational logic within `switch`:
    ```matlab
    x = 3, y = 3;
    switch x
        case x*(x==y)
            disp('x and y are equal');
        case x*(x>y)
            disp('x is greater than y');
        otherwise
            disp('x is less than y');
    end
    ```
  - Mechanism: When $x == y$ is true ($1$), `x*(x==y)` equals $x \times 1 = x$, matching `switch x`.

---

### [M3-MAIN - Modeling Continuous Systems-page-65.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-65.png)
- **Slide Title:** The Menu Function
- **Key Concepts & Code:**
  - `menu(title_str, opt1, opt2, ...)` creates a pop-up graphical dialog with pushbuttons and returns an integer corresponding to the chosen button ($1, 2, \dots$):
    ```matlab
    pick = menu('Pick a Pizza','Cheese','Sausage','Mushroom');
    switch pick
        case 1
            disp('Order a cheese pizza')
        case 2
            disp('Order a Sausage pizza')
        case 3
            disp('Order a Mushroom pizza')
        otherwise
            disp('No pizza for us today')
    end
    ```
  - Selecting `'Sausage'` returns $2$, producing `Order a sausage pizza`.

---

### [M3-MAIN - Modeling Continuous Systems-page-66.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-66.png)
- **Slide Title:** Selection and Looping Statements / The For Loop
- **Key Concepts & Code:**
  - General syntax:
    ```matlab
    for loopvar = range
        action
    end
    ```
  - Variations shown:
    - Consecutive integer loop: `for a = 10:20` $\rightarrow$ prints $10$ to $20$.
    - Index array loop: `for v = [1:10]` $\rightarrow$ `disp(v)`.
    - Explicit list of arbitrary numbers: `for v = [1 5 8 17]` $\rightarrow$ `disp(v)`.
    - Decrementing loop: `for v = 1.0:-0.2:0.0` $\rightarrow$ iterates down from $1.0$ to $0.0$ by $-0.2$.
    - Fixed iteration count for repetition: `for v = [1:10]` $\rightarrow$ `disp("Hello")` prints 10 times.

---

### [M3-MAIN - Modeling Continuous Systems-page-67.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-67.png)
- **Slide Title:** Selection and Looping Statements / The While Loop
- **Key Concepts & Code:**
  - General syntax: `while <expression>` $\dots$ `<statements>` $\dots$ `end`.
  - **Example 1:**
    ```matlab
    a = 10;
    while( a < 20 )
        fprintf('value of a: %d\n', a);
        a = a + 1;
    end
    ```
    - Prints values $10$ through $19$.
  - **Example 2 (`break`):**
    - Terminates loop prematurely when `if( a > 15 ) break; end`.
    - Prints values $10$ through $15$.
  - **Example 3 (`continue`):**
    - Starts with $a = 9$. Increments $a = a + 1$ first.
    - When `if a == 15 continue; end`, skipping print statement.
    - Output values: $10, 11, 12, 13, 14, 16, 17, 18, 19, 20$.

---

### [M3-MAIN - Modeling Continuous Systems-page-68.png](file:///D:/School-Works/Modeling%20and%20Simulation/ModSim%20Exam%20Prep/sources/picture_notes/img/M3-MAIN%20-%20Modeling%20Continuous%20Systems-page-68.png)
- **Slide Title:** References
- **Sources Listed:**
  - Online: `www.tutorialspoint.com`
  - E-Books and Textbooks:
    - Attaway, Stormy (2013). *MATLAB ®: A Practical Introduction to Programming and Problem Solving*, Third Edition. Elsevier, Inc.

---

### Possible slide errors

1. **Slide 61:**
   - **Syntax Error (`.x`):** The left script starts with `.x = input(...)`. In MATLAB, a variable name cannot begin with a leading period (`.`), resulting in a syntax error.
   - **Invalid Modulo Operator (`%`):** The script writes `y = x % 2;`. In MATLAB, `%` designates the beginning of a comment. To perform a modulo remainder operation, the built-in functions `mod(x, 2)` or `rem(x, 2)` must be used.
   - **Logic Copy-Paste Bug:** In the odd/even snippet on the right, the `else` branch contains `fprintf('Even number');` instead of `'Odd number'`. Both branches print "Even number".
   - **Incomplete Zero Handling:** In the positive/negative check, when $x = 0$, the condition `x < 0` evaluates to false, causing $0$ to be incorrectly classified as `"Positive"`.

2. **Slide 62:**
   - **Uncovered Boundary Ages:** The conditions test `age > 0 && age <= 13`, then `elseif age > 13 && age < 20`, followed by `elseif age > 20 && age < 60`. Integer ages of exactly `20` and `60` fall into neither condition and fall through to subsequent checks (`age = 20` falls into `senior` because $20 \le 100$, and `age = 60` also falls into `senior`).
   - **Negative Age Fallthrough:** If an invalid negative age is entered (e.g., `-5`), `age > 0 && age <= 13` fails, but `-5 <= 100` evaluates to true, improperly categorizing negative numbers as `"senior"`.

3. **Slide 65:**
   - **Typo in Button Label:** In the dialog screenshot, the third button label displays `"Shroom"` instead of `"Mushroom"` as passed into the `menu` function call.
   - **Typo in Comment:** The comment states `"%This is script as the user for a type of pizza"`, which is missing the word "asks" ("asks the user").
