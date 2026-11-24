Here are the structured study notes for each of the 25 slides, followed by the compiled list of possible slide errors.

---

### `img/M2-MAIN-Discrete Event Simulation-page-1.png`
* **Slide Title:** Modeling and Simulation
* **Key Content:**
  * Course introductory cover slide.
  * Institutional affiliation: FEU Alabang, FEU Diliman, FEU Tech.
  * Slogan: *"Technology Driven by Innovation"*.

---

### `img/M2-MAIN-Discrete Event Simulation-page-2.png`
* **Slide Title:** MODULE 2: DISCRETE EVENT SIMULATION
* **Key Content:**
  * Module header establishing the core topic: Discrete Event Simulation (DES).

---

### `img/M2-MAIN-Discrete Event Simulation-page-3.png`
* **Slide Title:** SUBTOPIC 1: STATISTICAL CONCEPTS FOR DES
* **Key Content:**
  * Section title covering essential statistical foundations used in DES.

---

### `img/M2-MAIN-Discrete Event Simulation-page-4.png`
* **Slide Title:** OBJECTIVES
* **Key Content:**
  * Understand statistical concepts required to build and apply DES models.
  * Incorporate randomness into system models via statistical techniques.
  * Process and evaluate simulation output to assess system performance.
  * Recall set and function properties underpinning probability spaces.
  * Investigate input data modeling (stochastic inputs) and output data analysis.

---

### `img/M2-MAIN-Discrete Event Simulation-page-5.png`
* **Slide Title:** PROBABILITY
* **Key Content:**
  * Probability serves as the foundational building block for statistics.
  * Statistics supplies methods to:
    1. Represent real-world randomness.
    2. Generate streams of random variates that drive stochastic simulations.
    3. Analyze and interpret output data produced by simulation experiments.

---

### `img/M2-MAIN-Discrete Event Simulation-page-6.png`
* **Slide Title:** Probability - Sets
* **Key Content:**
  * **Set:** A collection of objects, typically designated with capital letters.
  * **Element ($\in$):** Individual objects comprising the set.
  * **Null / Empty Set ($\Phi$ or $\{\}$):** A set containing zero elements.
  * **Examples:** $S = \{x, y, z\}$, $x \in S$, $A = \{\}$.
  * **Core rules:** Sets contain distinct elements (no duplicates); any given object either belongs to a set or does not.

---

### `img/M2-MAIN-Discrete Event Simulation-page-7.png`
* **Slide Title:** Probability - Sets (Set Characteristics)
* **Key Content:**
  1. **Countable:** Elements can be placed in 1-to-1 correspondence with the positive integers.
  2. **Finite:** Empty or has elements that can be counted with termination; otherwise **infinite**.
  3. **Subset ($A \subseteq B$):** Every element in $A$ is also contained in $B$.
  4. **Disjoint:** Two sets sharing no common elements ($A \cap B = \emptyset$).
  5. **Universal Set ($U$):** The complete reference set encompassing all items in a given context.
  6. **Equal Sets ($A = B$):** Both sets contain identical elements.

---

### `img/M2-MAIN-Discrete Event Simulation-page-8.png`
* **Slide Title:** Probability - Sets (Set Operations)
* **Key Content:**
  1. **Union ($A \cup B$):** Elements belonging to $A$, $B$, or both.
  2. **Intersection ($A \cap B$):** Elements belonging to both $A$ and $B$.
  3. **Difference ($A - B$):** Elements in $A$ that do not belong to $B$. Note: generally, $A - B \neq B - A$.
  4. **Complement ($A^C$):** $U - A$ (all elements in universal set $U$ outside $A$).

---

### `img/M2-MAIN-Discrete Event Simulation-page-9.png`
* **Slide Title:** Probability - Sets (Example)
* **Given Data:**
  * Universal Set: $U = \{2, 4, 6, 8, 10, 12\}$
  * Sets: $A = \{2, 4, 10\}$, $B = \{4, 6, 8, 10\}$
* **Calculated Operations:**
  * $A \cup B = \{2, 4, 6, 8, 10\}$
  * $A \cap B = \{4, 10\}$
  * $A^C = \{6, 8, 12\}$
  * $A - B = \{2\}$
  * $B - A = \{6, 8\}$

---

### `img/M2-MAIN-Discrete Event Simulation-page-10.png`
* **Slide Title:** Probability - Functions
* **Key Content:**
  * A function consists of three components:
    1. Domain set $X$
    2. Codomain set $Y$
    3. Rule of correspondence $f$ mapping each domain element to exactly one codomain element.
  * **Notation:** $f: X \rightarrow Y$ or $f(x) = y$ for $x \in X$, $y \in Y$.
  * Two functions are equal if and only if their domains, codomains, and rules of correspondence match.

---

### `img/M2-MAIN-Discrete Event Simulation-page-11.png`
* **Slide Title:** Probability - Functions (Properties of Functions)
* **Key Content:**
  1. **Range:** Subset of codomain $Y$ mapped to by elements of domain $X$ under $f$.
  2. **Onto (Surjective):** Range equals the entire codomain ($f(X) = Y$).
  3. **One-to-One (Injective):** Distinct domain elements map to distinct codomain elements.
  4. **Inverse ($f^{-1}$):** Exists if and only if $f$ is bijective (both one-to-one and onto).
  5. **Inverse Mapping:** $f^{-1}: Y \rightarrow X$ where $f^{-1}[f(x)] = x$ for all $x \in X$.

---

### `img/M2-MAIN-Discrete Event Simulation-page-12.png`
* **Slide Title:** Probability - Functions (Example)
* **Key Content:**
  * Domain $X = \mathbb{R}$, Codomain $Y = \mathbb{R}$, rule: $y = f(x) = mx + b$ ($m, b \in \mathbb{R}$).
  * **Case $m \neq 0$:** Linear function is bijective (one-to-one and onto).
    * Inverse: $x = f^{-1}(y) = \frac{1}{m}y - \frac{b}{m}$.
  * **Case $m = 0$:** Constant line $y = b$.
    * Range is single element $\{b\}$; neither injective nor surjective; inverse does not exist.
  * Graph shows a straight line with slope $m$ crossing the vertical axis at $b$.

---

### `img/M2-MAIN-Discrete Event Simulation-page-13.png`
* **Slide Title:** PROBABILITY - Probability Space
* **Key Content:**
  * Core construct for formalizing probabilistic problems.
  * Defined as a triple of three components:
    * a) Sample space $S$
    * b) $\sigma$-algebra of events $A$
    * c) Probability measure $P$

---

### `img/M2-MAIN-Discrete Event Simulation-page-14.png`
* **Slide Title:** PROBABILITY - Probability Space
* **Key Content:**
  * **Random Experiment:** An experiment whose specific outcome cannot be predicted beforehand.
  * **Sample Space ($S$):** The set containing all possible outcomes of a random experiment.
  * **Event ($E$):** Any subset of the sample space ($E \subseteq S$).

---

### `img/M2-MAIN-Discrete Event Simulation-page-15.png`
* **Slide Title:** PROBABILITY - Probability Space
* **Key Content:**
  * **$\sigma$-algebra of events ($A$):** A collection of subsets of $S$ satisfying:
    1. If $E \in A$, then $E^C \in A$ (closed under complement).
    2. If $E_1, E_2 \in A$, then $E_1 \cup E_2 \in A$ (closed under union).
    3. If $E_1, E_2 \in A$, then $E_1 \cap E_2 \in A$ (closed under intersection).
    4. $S \in A$ (contains the sample space).
  * **Discrete size rule:** If discrete sample space $S$ contains $k$ outcomes, its full power set $\sigma$-algebra contains $2^k$ events.

---

### `img/M2-MAIN-Discrete Event Simulation-page-16.png`
* **Slide Title:** PROBABILITY - Probability Space
* **Key Content:**
  * **Probability Measure ($P$):** A function with domain $A$ and codomain $[0, 1] \subset \mathbb{R}$ satisfying:
    1. Non-negativity: $P(E) \ge 0$ for all $E \in A$.
    2. Normalization: $P(S) = 1$.
    3. Additivity: $P(E_1 \cup E_2) = P(E_1) + P(E_2)$ when $E_1 \cap E_2 = \emptyset$.

---

### `img/M2-MAIN-Discrete Event Simulation-page-17.png`
* **Slide Title:** PROBABILITY - Probability Space
* **Example Scenario:**
  * A 3-sided die with faces labeled $B, C, D$.
  * Experimental outcome probabilities:
    * $P(\text{Side } B) = \frac{1}{6}$
    * $P(\text{Side } C) = \frac{1}{3}$
    * $P(\text{Side } D) = \frac{1}{2}$
  * Sample space: $S = \{B, C, D\}$.

---

### `img/M2-MAIN-Discrete Event Simulation-page-18.png`
* **Slide Title:** PROBABILITY - Probability Space
* **Example Resolution:**
  * Number of events: $k = 3 \implies 2^3 = 8$ events.
  * $\sigma$-algebra:
    $$A = \{\emptyset, \{B\}, \{C\}, \{D\}, \{B, C\}, \{B, D\}, \{C, D\}, \{B, C, D\}\}$$
  * Probability Measure Table:
    * $\Phi \rightarrow 0$
    * $\{B\} \rightarrow 1/6$
    * $\{C\} \rightarrow 1/3$
    * $\{D\} \rightarrow 1/2$
    * $\{B, C\} \rightarrow 1/6 + 1/3 = 1/2$
    * $\{B, D\} \rightarrow 1/6 + 1/2 = 2/3$
    * $\{C, D\} \rightarrow 1/3 + 1/2 = 5/6$
    * $S \rightarrow 1$

---

### `img/M2-MAIN-Discrete Event Simulation-page-19.png`
* **Slide Title:** PROBABILITY - Random Variables
* **Key Content:**
  * **Random Variable ($X$):** A mapping/function assigning real numbers to experimental outcomes ($s \in S \mapsto X(s) \in \mathbb{R}$).
  * Structure:
    * Domain: $S$
    * Codomain: $\mathbb{R}$
    * Measurability condition: $\{X \le x\} = \{s \mid s \in S \text{ and } X(s) \le x\}$ must belong to event space $A$ for all $x \in \mathbb{R}$.

---

### `img/M2-MAIN-Discrete Event Simulation-page-20.png`
* **Slide Title:** PROBABILITY - Random Variables
* **Key Content:**
  * **Cumulative Distribution Function (CDF), $F(x)$:**
    * Domain: $\mathbb{R}$, Codomain: $[0, 1] \subset \mathbb{R}$.
    * Rule: $F(x) = P(\{X(s) \le x\})$.
  * **Properties:**
    1. $F(-\infty) = 0$ and $F(+\infty) = 1$.
    2. $0 \le F(x) \le 1$ for all $x \in \mathbb{R}$.
    3. Nondecreasing: $F(x_1) \le F(x_2)$ whenever $x_1 < x_2$.
    4. Right-continuous: $\lim_{h \to 0^+} F(x+h) = F(x)$ (written $F(x^+) = F(x)$).
    5. Interval probability: $P(x_1 < X \le x_2) = F(x_2) - F(x_1)$.

---

### `img/M2-MAIN-Discrete Event Simulation-page-21.png`
* **Slide Title:** PROBABILITY - Random Variables
* **Example (Three-sided die CDF):**
  * Variable assignment: $X(B) = 1$, $X(C) = 2$, $X(D) = 3$.
  * Event mapping:
    * $\{X(s) < 1\} = \Phi$
    * $\{X(s) < 2\} = \{B\}$
    * $\{X(s) < 3\} = \{B, C\}$
    * $\{X(s) < \infty\} = S$
  * CDF formula:
    $$F(x) = \sum_{k=1}^3 P(x_k)u(x - x_k)$$
  * Step function definition shown:
    $$u(x) = \begin{cases} 1 & x > 0 \\ 0 & x < 0 \end{cases}$$
  * Step graph levels: jump to $1/6$ at $x=1$, jump to $1/2$ at $x=2$, jump to $1$ at $x=3$.

---

### `img/M2-MAIN-Discrete Event Simulation-page-22.png`
* **Slide Title:** PROBABILITY - Random Variables
* **Key Content:**
  * **Probability Density Function (PDF), $f(x)$:**
    * Domain: $\mathbb{R}$, Codomain: $\mathbb{R}$.
    * Relationship: $f(x) = \frac{dF(x)}{dx}$.
  * **Properties:**
    1. Non-negativity: $f(x) \ge 0$ for all $x \in \mathbb{R}$.
    2. Total area under curve: $\int_{-\infty}^\infty f(x) dx = 1$.
    3. CDF from PDF: $F(x) = \int_{-\infty}^x f(\sigma) d\sigma$.
    4. Interval probability: $P(x_1 < X \le x_2) = \int_{x_1}^{x_2} f(x) dx$.

---

### `img/M2-MAIN-Discrete Event Simulation-page-23.png`
* **Slide Title:** SIMULATION BASICS (Theoretical Distribution Functions Used Commonly in M&S)
* **1. Uniform Distribution:**
  * Models equally likely outcomes over a finite interval $[a, b]$.
  * Denoted $UNIFORM(a, b)$ with $-\infty < a < b < \infty$.
  * PDF:
    $$f(x) = \begin{cases} \frac{1}{b-a} & a \le x \le b \\ 0 & \text{otherwise} \end{cases}$$
  * Graph: Flat rectangular box of constant height $\frac{1}{b-a}$ between $x = a$ and $x = b$.

---

### `img/M2-MAIN-Discrete Event Simulation-page-24.png`
* **Slide Title:** SIMULATION BASICS (Theoretical Distribution Functions Used Commonly in M&S)
* **2. Triangular Distribution:**
  * Used when exact distribution is unknown, but minimum ($a$), mode ($m$), and maximum ($b$) are estimable ($a < m < b$).
  * Denoted $TRIANGULAR(a, m, b)$.
  * PDF:
    $$f(x) = \begin{cases} \frac{2}{(b-a)(m-a)}(x - a) & a \le x \le m \\ \frac{2}{(b-a)(b-m)}(b - x) & m \le x \le b \\ 0 & \text{otherwise} \end{cases}$$
  * Graph: Triangle starting at 0 at $a$, peaking at mode $m$, and returning to 0 at $b$.

---

### `img/M2-MAIN-Discrete Event Simulation-page-25.png`
* **Slide Title:** SIMULATION BASICS (Theoretical Distribution Functions Used Commonly in M&S)
* **3. Exponential Distribution:**
  * Frequently models interarrival times in queuing/DES systems.
  * Denoted $EXPONENTIAL(m)$, where $m$ is the mean ($0 < m < \infty$).
  * Parameters: Rate $\lambda$ is average number of events per unit time; mean $m = \frac{1}{\lambda}$.
  * Formulas shown:
    $$f(x) = \begin{cases} e^{-\lambda x} & x \ge 0 \\ 0 & \text{otherwise} \end{cases}$$
    $$P(X > x) = e^{-\lambda x}, \quad P(X < x) = 1 - e^{-\lambda x}$$
  * Graph: Strictly decreasing decay curve starting on the vertical axis and decaying toward zero.

---

### Possible slide errors

1. **Slide 6:** The null set is denoted using the uppercase Greek letter $\Phi$ ("$\Phi$ or $\{\}$") instead of the standard empty set symbol $\emptyset$.
2. **Slide 7 (Item 1):** Countable is defined as *"can be put in a one-to-one correspondence with the positive integers"*. In standard mathematics, this specifically defines a *countably infinite* (denumerable) set. A countable set in general can be either finite or countably infinite.
3. **Slide 7 (Item 2):** Grammatical omission in bullet 2: *"elements that can counted"* is missing the auxiliary verb "be" (should read *"can be counted"*).
4. **Slide 11 (Item 2):** Typo in bullet 2: *"is said to onto"* is missing "be" (should read *"is said to be onto"*).
5. **Slide 11 (Items 4 & 5) & Slide 12:** The notation for the inverse function is erroneously typed as $f^1$, $f^1: Y \rightarrow X$, and $x = f^1(y)$ using positive exponent 1 rather than negative exponent $-1$ ($f^{-1}$, $f^{-1}: Y \rightarrow X$, $x = f^{-1}(y)$).
6. **Slide 19:** Overloaded notation: The probability space tuple is defined as $\mathbf{P} = (S, A, P)$ using $P$ both for the overall space and the probability measure itself (standard notation typically uses $(\Omega, \mathcal{F}, P)$ or $(S, A, P)$ where the space is denoted by a distinct symbol, e.g., $\mathcal{S}$).
7. **Slide 21:**
   * In the bottom-left event breakdown, strict inequalities are used: $\{X(s) < 1\} = \Phi$, $\{X(s) < 2\} = \{B\}$, $\{X(s) < 3\} = \{B, C\}$. Standard CDFs are defined using non-strict inequalities ($\le$), which contradicts the accompanying right-continuous step plot where the jumps occur at the points ($F(1) = 1/6, F(2) = 1/2, F(3) = 1$).
   * The unit step function $u(x)$ definition completely omits $x = 0$ ($u(x) = 1$ for $x > 0$, $0$ for $x < 0$). For CDFs to be right-continuous, the Heaviside step function must be defined as $u(x) = 1$ for $x \ge 0$.
8. **Slide 25:**
   * **Missing Rate in PDF:** The probability density function is written as $f(x) = e^{-\lambda x}$ for $x \ge 0$. This does not integrate to 1 (it integrates to $\frac{1}{\lambda}$). The correct PDF is $f(x) = \lambda e^{-\lambda x}$ (or $\frac{1}{m} e^{-x/m}$).
   * **Incorrect Graph Y-Intercept:** The vertical intercept of the density curve on the graph is labeled as $m$. The value of the exponential density at $x = 0$ is $f(0) = \lambda = \frac{1}{m}$, not the mean $m$. Labeling the intercept as $m$ wrongly suggests that a larger mean would produce a taller initial peak, when in reality larger means flatten the curve.

Here are the study notes for the requested slides, followed by the list of possible slide errors.

---

### `img/M2-MAIN-Discrete Event Simulation-page-26.png`
* **Slide Title:** SIMULATION BASICS – Theoretical Distribution Functions Used Commonly in M&S: 4. Normal Distribution
* **Key Facts & Concepts:**
  * Models variation around a central mean value.
  * Represents the distribution of the sum of many independent random variables (Central Limit Theorem), even if individual variables are non-normal.
  * Bell-shaped, symmetric curve centered at the mean.
* **Notation & Formulas:**
  * Notation: $NORMAL(m, \sigma)$
  * Parameters: Mean $m \in \mathbb{R}$ ($-\infty < m < \infty$), standard deviation $\sigma \in \mathbb{R}$ ($0 < \sigma < \infty$).
  * Probability Density Function (PDF):
    $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$

---

### `img/M2-MAIN-Discrete Event Simulation-page-27.png`
* **Slide Title:** SIMULATION BASICS – Generation of Random Variates
* **Key Facts & Concepts:**
  * **Random Variates:** Independent sample values drawn from a random variable governed by a specific theoretical distribution.
  * Fast and efficient random variate generation is a core capability required of all Discrete Event Simulation (DES) software.
  * **Two-Step Generation Process:**
    1. A random number is generated.
    2. The random number is transformed into a random variate.

---

### `img/M2-MAIN-Discrete Event Simulation-page-28.png`
* **Slide Title:** SIMULATION BASICS – Generation of Random Variates (Step 1 Details)
* **Key Facts & Concepts:**
  * Detailed breakdown of Step 1:
    * A random number is drawn from the continuous standard uniform distribution: $UNIFORM(0, 1)$.
    * A real number in the range $[0, 1]$ where every value has an equal likelihood of being chosen.
  * Step 2 subsequently maps this uniform value into the desired distribution variate.

---

### `img/M2-MAIN-Discrete Event Simulation-page-29.png`
* **Slide Title:** SIMULATION BASICS – Generation of Random Variates (Linear Congruential Generators)
* **Key Facts & Concepts:**
  * Computers generate pseudorandom sequences using recursive algorithms, predominantly the **Linear Congruential Generator (LCG)**.
  * Values are integers constrained to the interval $0 \le Z_k \le m - 1$.
* **Formulas & Parameters:**
  * Recursive generator formula:
    $$Z_k = (a Z_{k-1} + c) \pmod m$$
  * Parameters:
    * $a$: constant multiplier (nonnegative integer)
    * $c$: increment (nonnegative integer)
    * $m$: modulus (nonnegative integer)
    * $Z_0$: initial seed value
  * Transformation to uniform $(0, 1)$ random number $U_k$:
    $$U_k = \frac{Z_k}{m}$$

---

### `img/M2-MAIN-Discrete Event Simulation-page-30.png`
* **Slide Title:** SIMULATION BASICS – LCG (Cycle Length)
* **Key Facts & Concepts:**
  * An initial seed $Z_0$ generates a sequence of $p$ distinct integers before repeating, where period length $p \le m$.
  * **Full-cycle / full-period generator:** Occurs when $p = m$ (all values from $0$ to $m-1$ appear before repeating).
  * Simulation requires choosing parameters and seed carefully to maximize cycle length.
* **Sequence Values Shown ($m = 16$):**
  * `1, 6, 15, 12, 13, 2, 11, 8, 9, 14, 7, 4, 5, 10, 3, 0`
  * Citation: Olivar, A. (2015). *Stochastic Simulation of Random Numbers Using Linear Congruential Method*.

---

### `img/M2-MAIN-Discrete Event Simulation-page-31.png`
* **Slide Title:** SIMULATION BASICS – LCG (Hull-Dobell Full-Cycle Conditions)
* **Key Facts & Conditions (Hull & Dobell, 1962):**
  1. Increment $c$ is relatively prime to modulus $m$ ($\gcd(c, m) = 1$).
  2. Every prime factor of $m$ divides $(a - 1)$.
  3. If 4 divides $m$, then 4 must also divide $(a - 1)$.
* **Example Demonstrated:**
  * Parameters: $a = 1, c = 3, m = 20, \text{Seed } Z_0 = 2$
  * Validation:
    * $\gcd(3, 20) = 1$ (Satisfied)
    * Prime factors of 20 (2 and 5) divide $(1 - 1 = 0)$ (Satisfied)
    * 4 divides 20, and 4 divides $(1 - 1 = 0)$ (Satisfied)
  * Generated sequence positions 1 through 20:
    * `5, 8, 11, 14, 17, 0, 3, 6, 9, 12, 15, 18, 1, 4, 7, 10, 13, 16, 19, 2`

---

### `img/M2-MAIN-Discrete Event Simulation-page-32.png`
* **Slide Title:** INPUT DATA MODELING – Components in the development of a system model
* **Key Facts & Components:**
  1. **Structural Modeling:** Defines the physical/logical components (entities, locations, resources, routing/processes) producing structural representations such as queuing networks.
  2. **Data Modeling:** Establishes the quantitative parameters needed to drive the structural model (e.g., interarrival distributions, process service times, failure rates, resource shifts, transit delays).

---

### `img/M2-MAIN-Discrete Event Simulation-page-33.png`
* **Slide Title:** INPUT DATA MODELING – Choice for generating the random variate stream required for simulation
* **Key Facts:**
  * Three foundational strategies available:
    1. Direct Use of Sample Data
    2. Use of Empirical Distribution
    3. Use of Theoretical Distribution

---

### `img/M2-MAIN-Discrete Event Simulation-page-34.png`
* **Slide Title:** INPUT DATA MODELING – Direct Use of Sample Data
* **Key Facts:**
  * Involves replaying collected observations directly from a storage file.
  * **Advantage:** Guarantees every generated value is completely legal and realistic.
  * **Disadvantages:**
    * Limited sample size omits rare or tail events.
    * Repeated disk/memory lookups introduce significant computational overhead.
    * A simulation run typically demands far more data points than collected samples.
  * Rarely employed in practical simulation studies.

---

### `img/M2-MAIN-Discrete Event Simulation-page-35.png`
* **Slide Title:** INPUT DATA MODELING – Use of Empirical Distribution
* **Key Facts:**
  * Nonparametric distribution formed directly from observed sample data.
  * **Advantages:**
    * Generates arbitrary-length streams of variates.
    * Readily maps random numbers to representative variates.
    * Keeps all values realistic and valid.
  * **Disadvantage:** Cannot extrapolate to unobserved values or tail extremes beyond sample bounds.
  * Preferred when sample data cannot be adequately fitted to standard theoretical distributions.

---

### `img/M2-MAIN-Discrete Event Simulation-page-36.png`
* **Slide Title:** INPUT DATA MODELING – Use of Theoretical Distribution
* **Key Facts:**
  * Defined mathematically through specific distribution parameters controlling location, scale, and shape.
  * **Common Examples:**
    * Exponential Distribution
    * Normal Distribution
    * Triangular Distribution

---

### `img/M2-MAIN-Discrete Event Simulation-page-37.png`
* **Slide Title:** INPUT DATA MODELING – Use of Theoretical Distribution (Evaluation)
* **Key Facts:**
  * **Advantages:**
    * Smooths sampling noise and irregularities caused by limited sample sets.
    * Highly computationally efficient to evaluate during simulation runs.
  * **Disadvantage:** Demands parameter estimation/fitting effort, and some real-world data patterns defy good theoretical fits.

---

### `img/M2-MAIN-Discrete Event Simulation-page-38.png`
* **Slide Title:** INPUT DATA MODELING – Categorization of input data modeling situations
* **Taxonomy Chart:**
  * **System data:**
    * **Simple data:**
      * Use sample data
      * Empirical distribution
      * Theoretical distribution
    * **Complex data:**
      * No data available
      * Multimodal data
      * Correlated data
      * Nonstationary data

---

### `img/M2-MAIN-Discrete Event Simulation-page-39.png`
* **Slide Title:** OUTPUT DATA ANALYSIS – Output Data Analysis
* **Key Facts:**
  * **Definition:** Analyzing raw simulation output data to infer system performance metrics.
  * **Planned Steps:**
    1. Queuing example demonstrating why statistical analysis of output is necessary.
    2. Confidence interval estimation for mean performance metrics.
    3. Review of complex output scenarios and techniques to handle them.

---

### `img/M2-MAIN-Discrete Event Simulation-page-40.png`
* **Slide Title:** Formative Assessment 2
* **Key Facts:**
  * Assessment placeholder slide instructing students to consult Canvas for instructions.

---

### `img/M2-MAIN-Discrete Event Simulation-page-41.png`
* **Slide Title:** SUBTOPIC 2 – DISCRETE EVENT SIMULATION
* **Key Facts:**
  * Section divider slide introducing Subtopic 2: Discrete Event Simulation.

---

### `img/M2-MAIN-Discrete Event Simulation-page-42.png`
* **Slide Title:** OBJECTIVES
* **Key Facts:**
  * Core learning goals:
    * Understand foundational discrete event simulation concepts.
    * Discuss queuing model construction and performance metrics.
    * Illustrate DES methodology, execution mechanics, and general simulation architecture.

---

### `img/M2-MAIN-Discrete Event Simulation-page-43.png`
* **Slide Title:** OBJECTIVES
* **Key Facts:**
  * Competency statement: "After the completion of the topics and laboratory activities, students can:"
  * Re-states the three objectives from page 42 regarding understanding DES concepts, discussing queuing model construction/performance, and illustrating simulation methodology and mechanics.

---

### `img/M2-MAIN-Discrete Event Simulation-page-44.png`
* **Slide Title:** Discrete Event Simulation – What is Discrete Event Simulation (DES) ?
* **Key Facts:**
  * **Definition (Law: *Simulation Modeling and Analysis*):** Modeling a system as it evolves over time by a representation where state variables change instantaneously at separated points in time.
  * Physical system representation where state changes take place at exact discrete instants of simulated time.
  * **Core Characteristics:** DES is **stochastic**, **dynamic**, and **discrete**.

---

### `img/M2-MAIN-Discrete Event Simulation-page-45.png`
* **Slide Title:** Discrete Event Simulation – Example:
* **Key Facts & Model Mechanics:**
  * Train transit example between Station A and Station B:
    * Departure Event occurs at time `4:00 pm`.
    * Arrival Event occurs at time `6:00 pm`.
    * Transit movement between stations is treated as a single **Time Delay / Interval** (2 hours).
  * Continuous intermediate movement is abstracted away into two discrete boundary events.

---

### `img/M2-MAIN-Discrete Event Simulation-page-46.png`
* **Slide Title:** Discrete Event Simulation – Other Examples:
* **Key Facts:**
  * Visual representations of queuing systems:
    1. Patients queuing at a Medical Clinic.
    2. Customers queuing at an automated teller machine (ATM).

---

### `img/M2-MAIN-Discrete Event Simulation-page-47.png`
* **Slide Title:** Discrete Event Simulation – Other Examples:
* **Key Facts & Diagram:**
  * Diagram of standard single-server queuing system flow:
    $$\text{Customer arrival} \longrightarrow \text{Queue} \longrightarrow \text{Server} \longrightarrow \text{Customer departure}$$

---

### `img/M2-MAIN-Discrete Event Simulation-page-48.png`
* **Slide Title:** Discrete Event Simulation (Event Updates)
* **Key Facts:**
  * In DES, system state calculation only occurs when an event fires.
  * Example: In a queue, updates are triggered exclusively when an entity arrives or when an entity finishes service and departs. No state computation is needed during idle intervening intervals.

---

### `img/M2-MAIN-Discrete Event Simulation-page-49.png`
* **Slide Title:** Discrete Event Simulation (Application Domains)
* **Key Facts:**
  * Typical DES application areas:
    * Healthcare: Patient flow and queue management in hospitals.
    * Transportation: Vehicular traffic at intersections.
    * Industrial Engineering: Part and assembly routing along manufacturing lines.

---

### `img/M2-MAIN-Discrete Event Simulation-page-50.png`
* **Slide Title:** Discrete Event Simulation – Key Components of DES: 1. Entity
* **Key Facts & Diagrams:**
  * **Entity:** Dynamic object moving through the model that interacts with other entities or competes for constrained resources.
  * Illustrations:
    * Left: Two patient entities waiting for a single medical resource (doctor/nurse).
    * Right: Hierarchical agent interaction diagram showing student entities traversing a DES course process embedded within a school agent.

---

### Possible Slide Errors

1. **Slide 26 – Parameter Inconsistency in Normal Distribution Formula:**
   * In the parameter definitions, the mean is denoted as $m$ ("where: m – the mean of the distribution", $NORMAL(m, \sigma)$). However, the probability density function formula directly beneath uses standard Greek letter $\mu$ in the exponent:
     $$e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$
     instead of $m$. The notation should consistently use either $m$ or $\mu$.

2. **Slide 31 – Conflation of Prime Factors with Prime Factorization:**
   * Under condition 2, the slide reads: *"Each prime factor of m 20 (2 x 2 x 5) divides a – 1"*. The set of distinct prime factors of 20 is $\{2, 5\}$. Writing $2 \times 2 \times 5$ represents the prime factorization product ($2^2 \times 5$), not each prime factor.

3. **Slide 37 – Grammatical Typo:**
   * Under Advantage (b), the text states: *"Use of this approach is computational efficient."* The adjective "computational" should be the adverb **"computationally"** to properly modify the adjective "efficient".

4. **Slides 42 & 43 – Redundant Duplicate Slide:**
   * Slide 43 duplicates Slide 42 almost verbatim. Slide 42 lists the three course objectives, and Slide 43 repeats the exact same three bullet points simply preceded by the sentence *"After the completion of the topics and laboratory activities, students can:"*. One of these slides is redundant.

5. **Slide 50 – Subject-Verb / Reciprocal Pronoun Agreement Error:**
   * The definition states: *"An object that can interact with each other or competes with each other for a resource."* A singular subject ("An object") cannot interact with or compete with "each other". It should properly be written in the plural (*"Objects that can interact with each other or compete for a resource"*) or rephrased (*"An object that can interact with other entities or compete for a resource"*).

### Study Notes: Discrete Event Simulation & Queuing Systems

---

#### **img/M2-MAIN-Discrete Event Simulation-page-51.png**
- **Slide Title:** Discrete Event Simulation - Key Components of DES (2. Attribute)
- **Key Facts:**
  - **Attribute:** A variable associated with an individual entity that travels with it throughout the simulation.
  - **Entity Memory:** In DES, an entity's history/experience through the system is preserved and represented by changes in its attribute values.
  - **Examples shown:** Age, Gender, Amount of Money, Health Status.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-52.png**
- **Slide Title:** Discrete Event Simulation - Key Components of DES (3. Resources)
- **Key Facts & Formulas:**
  - **Resource Capacity:** Total number of entities a resource can serve concurrently.
    - *Examples:* Single ATM capacity = $1$; Bank with 3 tellers capacity = $3$.
  - **Resource Utilization:** Key DES output metric measuring busy duration relative to total runtime.
  - **Formula:**
    $$\text{Resource Utilization} = \frac{\text{Busy time}}{\text{Total time}}$$

---

#### **img/M2-MAIN-Discrete Event Simulation-page-53.png**
- **Slide Title:** Discrete Event Simulation - Key Components of DES (4. Queue)
- **Key Facts:**
  - **Queue:** The waiting line/list an entity joins when a required resource is busy.
  - **Queue Logic / Disciplines:** FIFO, LIFO, HVF (Highest Value First).

---

#### **img/M2-MAIN-Discrete Event Simulation-page-54.png**
- **Slide Title:** Discrete Event Simulation - Key Components of DES (5. Events)
- **Key Facts:**
  - **Event:** Any instantaneous occurrence that alters the system state.
  - **Examples:**
    - Entity creation/arrival
    - Entity interaction or competition with another entity
    - Entity departure from the system

---

#### **img/M2-MAIN-Discrete Event Simulation-page-55.png**
- **Slide Title:** Discrete Event Simulation – Key Features
- **Key Facts:**
  - Implemented using general high-level programming languages (e.g., Pascal, C++) or specialized simulation packages.
  - **Five Core Features:**
    1. *Entities:* Representations of real-world elements (e.g., machine parts, people).
    2. *Relationships:* Linkages and interactions connecting entities.
    3. *Simulation Executive:* Controls clock advancement and triggers event routines.
    4. *Random Number Generator (RNG):* Produces stochastic inputs and variability.
    5. *Results & Statistics:* Evaluates performance measures and validates the model.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-56.png**
- **Slide Title:** Discrete Event Simulation – Simulation Methodology (Time Graph Representation)
- **Key Facts:**
  - The simulation clock / time counter tracks system time and initializes at zero ($0$).
  - **Two Clock Advance Mechanisms:**
    - *Time Slicing:* Updates system state at fixed, uniform time intervals regardless of event occurrence.
    - *Next Event:* Advances clock directly to the time of the next scheduled event; more computationally efficient than time slicing.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-57.png**
- **Slide Title:** Discrete Event Simulation – Simulation Methodology (Common Terminology Associated with DES)
- **Key Facts:**
  - **System State:** Collection of state variables describing system status at a specific instant.
  - **Simulation Clock:** Tracks elapsed simulated time.
  - **Next-Event List (FEL/NEL):** Chronologically ordered list of scheduled future event times.
  - **Statistical Counter / Accumulator:** Variables tracking and aggregating performance metrics over time.
  - **Initialization Subprogram:** Routine executed at time zero to configure initial states and schedule initial events.
  - **Timing Subprogram:** Determines the imminent event from the event list and advances the simulation clock to that event's timestamp.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-58.png**
- **Slide Title:** Discrete Event Simulation – Simulation Methodology (Common Terminology Associated with DES)
- **Key Facts:**
  - **Event Subprogram:** Specific routine invoked to execute system state changes when an event occurs.
  - **Library Subprogram:** Utility routines generating random variates from specified probability distributions.
  - **Report Generator:** Computes final statistical metrics and produces summary performance reports at termination.
  - **Main Program:** Orchestrator directing subprograms: calls timing, transfers control to event routines, checks termination conditions, and calls the report generator.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-59.png**
- **Slide Title:** Discrete Event Simulation – Simulation Methodology (DES Simulation Flowchart)
- **Key Facts & Logic:**
  - **Execution Sequence:**
    1. `Main program` $\rightarrow$ Condition: `Initial`?
    2. If `True` $\rightarrow$ invoke `Initialization subprogram` $\rightarrow$ return to `Main program`.
    3. If `False` $\rightarrow$ invoke `Timing subprogram` $\rightarrow$ invoke `Event subprogram`.
    4. Condition: `Library`? If `True` $\rightarrow$ call `Library subprogram` $\rightarrow$ return to `Event subprogram`.
    5. If `False` $\rightarrow$ Condition: `Stop`?
       - If `False` $\rightarrow$ loop back to `Main program`.
       - If `True` $\rightarrow$ call `Report generator` $\rightarrow$ End simulation.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-60.png**
- **Slide Title:** Discrete Event Simulation – Simulation Methodology (Classification of Systems)
- **Key Facts:**
  - **Discrete Systems:** State variables undergo instantaneous changes at discrete points in time ($t_1, t_2, t_3 \dots$).
    - *Example:* Customer count and server utilization at a fast-food restaurant during peak hours.
  - **Continuous Systems:** State variables change smoothly and continuously over time.
    - *Example:* Fluid volume continuously filling a tank.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-61.png**
- **Slide Title:** Discrete Event Simulation – Simulation Methodology (Approaches for Advancing the Simulation Clock: 1. Fixed-increment Advance)
- **Key Facts:**
  - Clock starts at zero and steps forward by uniform time increments ($\Delta t$).
  - Infrequently used in modern discrete simulation software.
  - Real events fall between step boundaries; event effects and state updates are artificially synchronized to the closest increment boundary.
  - Time increment size is subjective and introduces numerical approximation errors affecting performance metrics.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-62.png**
- **Slide Title:** Discrete Event Simulation – Simulation Methodology (Approaches for Advancing the Simulation Clock: 2. Next-Event Time Advance)
- **Key Facts:**
  - Dominant approach in DES software.
  - Clock initializes to zero and jumps directly to the timestamp of the earliest future event from the event list.
  - State variables are updated exactly when events occur.
  - Inactive intervening periods are bypassed, saving computation time.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-63.png**
- **Slide Title:** Queue (What causes queues?)
- **Key Facts:**
  - **Queue:** Line of customers awaiting service (e.g., banks, post offices, shipping ports, railway ticketing).
  - **Root Causes of Queueing:**
    - *Arrival Variation:* Non-uniform, irregular arrival timing.
    - *Service Variation:* Fluctuations in processing time per customer (brief vs. prolonged transactions).

---

#### **img/M2-MAIN-Discrete Event Simulation-page-64.png**
- **Slide Title:** Queuing System Model
- **Key Facts:**
  - Mathematical/conceptual representation quantifying waiting line behavior.
  - **Three Basic Elements:**
    1. *Entities:* Customers or arriving units.
    2. *Servers:* Service channels/stations processing entities.
    3. *Queues:* Buffers/holding lines where entities wait for service.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-65.png**
- **Slide Title:** Elements of Queuing Systems (1. Arrivals of Customers, 2. Service Mechanism)
- **Key Facts:**
  - **Arrivals:** Governed by random inter-arrival time distributions (*Arrival Pattern*).
  - **Service Mechanism:**
    - An idle server serves arriving customers immediately; busy servers cause customers to queue.
    - Successive service times are independent and identically distributed (IID) and independent of interarrival times.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-66.png**
- **Slide Title:** Elements of Queuing Systems (3. Queuing Discipline)
- **Key Facts:**
  - **Queue Discipline:** Policy determining the order of customer selection for service:
    - *FIFO / FCFS:* First In, First Out / First Come, First Served.
    - *LIFO / LCFS:* Last In, First Out / Last Come, First Served.
    - *Priority Queue:* Queues segmented by customer priority classes.
    - *SIRO:* Service In Random Order.
    - *STP (SPT):* Shortest process (processing) time.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-67.png**
- **Slide Title:** Approaches to modeling queues
- **Key Facts:**
  - **Analytic Models:** Solved via mathematical/differential equations; applicable to simple, tractable systems (e.g., stylized fast-food counter).
  - **Simulation Models:** Numerical evaluation designed for complex, multi-station configurations (e.g., Low Observable [LO] aircraft maintenance systems).

---

#### **img/M2-MAIN-Discrete Event Simulation-page-68.png**
- **Slide Title:** Why model queues?
- **Key Facts, Formulas & Table:**
  - Balances **Service Cost** (staffing/operating cost) vs. **Waiting Cost** (customer dissatisfaction, lost sales from balking/reneging).
  - **Formulas:**
    - $\text{Waiting Cost} = \text{Avg \# customers} \times \text{Avg wait time} \times \text{Cost per min}$
    - $\text{Service Cost} = \text{Number of Baristas} \times \text{Cost per barista}$
    - $\text{Total Expected Cost} = \text{Waiting Cost} + \text{Service Cost}$
  - **Parameters:** Avg customers = $5$; Cost per wait min = $\$10$; Cost per barista = $\$60$.
  - **Cost Tradeoff Table (Coffee Shop):**

| Number of Baristas | Avg Time Cust. Waits (min) | Waiting Costs | Service Cost | Total Expected Cost |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 7 | $5 \times 7 \times \$10 = \$350$ | $1 \times \$60 = \$60$ | \$410 |
| **2** | **4** | **$5 \times 4 \times \$10 = \$200$** | **$2 \times \$60 = \$120$** | **\$320 (Optimal Min)** |
| 3 | 3 | $5 \times 3 \times \$10 = \$150$ | $3 \times \$60 = \$180$ | \$330 |
| 4 | 2 | \$125 *(printed value)* | $4 \times \$60 = \$240$ | \$365 |

---

#### **img/M2-MAIN-Discrete Event Simulation-page-69.png**
- **Slide Title:** The Science of Queuing
- **Key Facts (Customer Behaviors):**
  - **Jockeying:** Switching between parallel lines in search of faster service.
  - **Reneging:** Leaving a queue after waiting without receiving service.
  - **Balking:** Deciding not to join a queue upon arrival due to excessive line length.
  - **Faffing:** Post-transaction delay while a customer packs up personal items before vacating the counter.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-70.png**
- **Slide Title:** The Science of Queuing (Arrival and Service Time, Arrival Process)
- **Key Facts:**
  - **Stochastic Behavior:** Characterized by randomness and non-deterministic variability.
  - **Arrival Process:** Governed by interarrival times between successive arrivals.
  - Successive interarrival times are independent and share an identical probability distribution.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-71.png**
- **Slide Title:** What are needed to model queues?
- **Key Facts:**
  - **Primary Parameters:**
    1. Arrival rate ($\lambda$)
    2. Service rate ($\mu$)
    3. Number of servers ($c$)
  - **Optional System Parameters:**
    4. Maximum queue capacity / length ($K$)
    5. Calling population size ($N$)

---

#### **img/M2-MAIN-Discrete Event Simulation-page-72.png**
- **Slide Title:** Types of Queues (1. Single Server, Single Phase)
- **Key Facts:**
  - Serves a single waiting line through a single processing stage (e.g., basic ATM, standard drive-thru kiosk).
  - Flow: $\text{Arrivals} \rightarrow \text{Queue} \rightarrow \text{Single Service Facility} \rightarrow \text{Departure}$.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-73.png**
- **Slide Title:** Types of Queues (2. Single Server, Multi Phase)
- **Key Facts:**
  - Sequential multiple service steps arranged in series (e.g., cafeteria/assembly line style like Chipotle).
  - Flow: $\text{Arrivals} \rightarrow \text{Queue} \rightarrow \text{Service Facility 1} \rightarrow \text{Service Facility 2} \rightarrow \text{Departure}$.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-74.png**
- **Slide Title:** Types of Queues (3. Multiple Server, Single Phase)
- **Key Facts:**
  - A single queue feeding into multiple parallel servers performing the same service (e.g., multi-teller bank line, Chick-fil-A order stations).
  - Flow: $\text{Arrivals} \rightarrow \text{Queue} \rightarrow \text{Parallel Facilities (1, 2, 3)} \rightarrow \text{Departure}$.

---

#### **img/M2-MAIN-Discrete Event Simulation-page-75.png**
- **Slide Title:** Types of Queues (4. Multiple Server, Multiple Phase)
- **Key Facts:**
  - Multiple parallel stations operating across multiple successive operational stages (e.g., laundromat with multiple washing machines followed by multiple dryers).
  - Flow: $\text{Arrivals} \rightarrow \text{Queue 1} \rightarrow \text{Parallel Facility 1 Stations} \rightarrow \text{Queue 2} \rightarrow \text{Parallel Facility 2 Stations} \rightarrow \text{Departure}$.

---

### Possible Slide Errors

1. **Slide 65 & Slide 70 – Incorrect Definition/Labeling of IID on "Arrival times":**
   - *Issue:* Slide 65 ("NOTE: IID means that the arrival times of the entities are independent...") and Slide 70 ("Arrival time: Independent... of each other and that the probability distribution is identical...") attribute the IID property to absolute *arrival times*.
   - *Why it is wrong:* Absolute arrival times ($T_n = \sum_{i=1}^n A_i$) are monotonically strictly increasing cumulative sums, meaning each arrival time is strongly dependent on prior arrival times and they do not share identical probability distributions. The property of being IID applies to **interarrival times** (the elapsed durations between arrivals), not absolute arrival times.

2. **Slide 66 – Typo in Queue Discipline Acronym:**
   - *Issue:* The second sub-bullet lists `"FIFO – Last in, First Out -> also called LCFS."`
   - *Why it is wrong:* "Last in, First Out" is abbreviated as **LIFO**, not FIFO. Additionally, "STP" is conventionally abbreviated as **SPT** (Shortest Processing Time).

3. **Slide 68 – Typo in Queueing Terminology ("Bulk"):**
   - *Issue:* Under Waiting Cost, the slide lists `"* Bulk : Leave without buying because the line is too long"`.
   - *Why it is wrong:* The correct queuing term is **Balking** (or *Balk*), which the presentation itself defines correctly on Slide 69 ("Balking: The customer decides not to enter the waiting line").

4. **Slide 68 – Arithmetic Inconsistency in Coffee Shop Cost Table:**
   - *Issue:* For 4 Baristas, the table lists an average wait of $2\text{ min}$, but reports Waiting Costs as **\$125**.
   - *Why it is wrong:* According to the formula stated in the table row ($\text{Avg \# cust.} \times \text{Avg. wait} \times \text{Cost wait}$, using $5\text{ customers}$ and $\$10/\text{min}$), the waiting cost should be $5 \times 2 \times \$10 = \mathbf{\$100}$, giving a total cost of $\$100 + \$240 = \mathbf{\$340}$ instead of $\$365$. A waiting cost of $\$125$ would require an average wait of $2.5\text{ minutes}$.

5. **Slide 69 – Incomplete Bullet Point:**
   - *Issue:* The final bullet point displays only `• FIFO` without any definition or explanation.
   - *Why it is wrong:* It is an unfinished slide artifact left over from editing.

6. **Slide 71 – Grammatical Error:**
   - *Issue:* Item 1 reads: `"How fast are customers will show up ?"`.
   - *Why it is wrong:* Grammatically erroneous phrasing mixing "are" and "will show up" (should read: *"How fast will customers show up?"* or *"How fast customers show up"*).

7. **Slide 73 & Slide 75 – Structural Mismatch / Subtitle Copy-Paste Error:**
   - *Issue on Slide 73:* Titled `"Single Server, Multi Phase"`, but the cartoon illustration shows three workers behind the counter, and Chipotle-style assembly setups feature dedicated staff at each phase (multi-server multi-phase or single-line multi-server phase).
   - *Issue on Slide 75:* Slide 75 uses the subtitle `"- Multiple servers serving a single line"`, which was copied verbatim from Slide 74. In the multi-server multi-phase schematic below it, customers transition through multiple sequential queues (Queue 1 and Queue 2), not a single line.

### Study Notes: Single-Server Queuing System (DES)

---

#### 1. [img/M2-MAIN-Discrete Event Simulation-page-76.png](file:///D:/School-Works/Modeling and Simulation/ModSim Exam Prep/sources/picture_notes/img/M2-MAIN-Discrete Event Simulation-page-76.png)
* **Slide Title:** Single-Server Queuing System - Parameters
* **Key Content:**
  * Displays the standard tabular layout/template used to track a single-server queue simulation by customer:
    * `Customer`
    * `Time service last arrival` [sic]
    * `Arrival Time`
    * `Service time`
    * `Time service begin`
    * `Waiting in queue`
    * `Time service ends`
    * `Time customer spends in system`
    * `Idle time of queue` [sic]

---

#### 2. [img/M2-MAIN-Discrete Event Simulation-page-77.png](file:///D:/School-Works/Modeling and Simulation/ModSim Exam Prep/sources/picture_notes/img/M2-MAIN-Discrete Event Simulation-page-77.png)
* **Slide Title:** Single-Server Queuing System - Parameters
* **Key Content & Formulas:**
  * **Formulas to be used:**
    1. $\text{Time since last arrival for } (i + 1) \text{ customer} = \text{Arrival time of } i^{\text{th}} \text{ customer} - \text{Arrival time of } (i - 1)^{\text{th}} \text{ customer}$
    2. $\text{Time customer wait in queue for } i^{\text{th}} \text{ customer} = \text{Arrival time of } i^{\text{th}} \text{ customer} - \text{Time service begin of } i^{\text{th}} \text{ customer}$
    3. $\text{Time service ends of } i^{\text{th}} \text{ customer} = \text{Time service begin of } i^{\text{th}} \text{ customer (min)} + \text{Service Time of } i^{\text{th}} \text{ customer}$
    4. $\text{Time customer spends in system} = \text{Time service ends of } i^{\text{th}} \text{ customer} - \text{Arrival time of } i^{\text{th}} \text{ customer}$
    5. $\text{Idle time of server for } i^{\text{th}} \text{ customer} = \text{Time service begins of } i^{\text{th}} \text{ customer} - \text{Time service ends of } (i - 1)^{\text{th}} \text{ customer}$
    6. **Time service begins:**
       * For first customer: $0$ (always stated on slide).
       * For subsequent customers: $\max(\text{Arrival of } i^{\text{th}} \text{ customer}, \text{Time service ends of } (i - 1)^{\text{th}} \text{ customer})$

---

#### 3. [img/M2-MAIN-Discrete Event Simulation-page-78.png](file:///D:/School-Works/Modeling and Simulation/ModSim Exam Prep/sources/picture_notes/img/M2-MAIN-Discrete Event Simulation-page-78.png)
* **Slide Title:** Single-Server Queuing System (Example)
* **Key Content & Input Table:**
  * Problem setup requiring parameter calculation for 6 customers.
  * **Input Data Table:**

| Parameter | Customer 1 | Customer 2 | Customer 3 | Customer 4 | Customer 5 | Customer 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Inter-arrival time (IAT) OR (AT)** | - | 4 | 1 | 4 | 2 | 4 |
| **Arrival time on clock** | 0 | 4 | 5 | 9 | 11 | 15 |
| **Service Time** | 2 | 3 | 1 | 4 | 2 | 3 |

---

#### 4. [img/M2-MAIN-Discrete Event Simulation-page-79.png](file:///D:/School-Works/Modeling and Simulation/ModSim Exam Prep/sources/picture_notes/img/M2-MAIN-Discrete Event Simulation-page-79.png)
* **Slide Title:** Single-Server Queuing System (Solution)
* **Completed Simulation Table:**

| Customer | Time since last arrival | Arrival Time | Service time | Time service begin | Waiting in queue | Time service ends | Time customer spends in system | Idle time of server |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | - | 0 | 2 | 0 | $(0 - 0) = 0$ | $(0 + 2) = 2$ | $(2 - 0) = 2$ | $0 - 0 = 0$ |
| **2** | 4 | 4 | 3 | 4 | $(4 - 4) = 0$ | $(4 + 3) = 7$ | $(7 - 4) = 3$ | $4 - 2 = 2$ |
| **3** | 1 | 5 | 1 | 7 | $(7 - 5) = 2$ | $(7 + 1) = 8$ | $(8 - 7) + 2 = 3$ or $8 - 5 = 3$ | $7 - 7 = 0$ |
| **4** | 4 | 9 | 4 | 9 | $(9 - 9) = 0$ | $(9 + 4) = 13$ | $(13 - 9) = 4$ | $9 - 8 = 1$ |
| **5** | 2 | 11 | 2 | 13 | $(13 - 11) = 2$ | $(13 + 2) = 15$ | $(15 - 13) + 2 = 4$ or $15 - 11 = 4$ | $13 - 13 = 0$ |
| **6** | 4 | 15 | 3 | 15 | $(15 - 15) = 0$ | $(15 + 3) = 18$ | $(18 - 15) = 3$ | $15 - 15 = 0$ |
| **Total** | **15** | | **15** | | **4** | | **19** | **3** |

---

#### 5. [img/M2-MAIN-Discrete Event Simulation-page-80.png](file:///D:/School-Works/Modeling and Simulation/ModSim Exam Prep/sources/picture_notes/img/M2-MAIN-Discrete Event Simulation-page-80.png)
* **Slide Title:** Formative Assessment 3
* **Key Content:**
  * Directive: "Check Canvas for instructions"
  * Visual graphic of a stack of books with service/business icons.

---

#### 6. [img/M2-MAIN-Discrete Event Simulation-page-81.png](file:///D:/School-Works/Modeling and Simulation/ModSim Exam Prep/sources/picture_notes/img/M2-MAIN-Discrete Event Simulation-page-81.png)
* **Slide Title:** Summative Assessment 2
* **Key Content:**
  * Directive: "Check Canvas for instructions"
  * Visual graphic of a stack of books with service/business icons.

---

#### 7. [img/M2-MAIN-Discrete Event Simulation-page-82.png](file:///D:/School-Works/Modeling and Simulation/ModSim Exam Prep/sources/picture_notes/img/M2-MAIN-Discrete Event Simulation-page-82.png)
* **Slide Title:** References
* **Key Content:**
  * **Online:** `www.tutorialspoint.com`
  * **E-Books and Textbooks:**
    * Sokolowski, John A. & Banks, Catherine M. (2010). *Modeling and Simulation Fundamentals Theoretical Underpinnings and Practical Domains*. John Wiley & Sons.

---

### Possible Slide Errors

1. **Slide 76, 78, and 79 – Table Column 2 Header:**
   * *Error:* Labeled `"Time service last arrival"`.
   * *Correction:* It should be `"Time since last arrival"` (inter-arrival time).

2. **Slide 76, 78, and 79 – Table Column 9 Header:**
   * *Error:* Labeled `"Idle time of queue"`.
   * *Correction:* It should be `"Idle time of server"`. A queue experiences waiting time or queue length, whereas the server experiences idle time when no customer is present.

3. **Slide 77 – Formula 1 (Index Mismatch):**
   * *Error:* Stated as $\text{Time since last arrival for } (i + 1) \text{ customer} = \text{Arrival time of } i^{\text{th}} \text{ customer} - \text{Arrival time of } (i - 1)^{\text{th}} \text{ customer}$.
   * *Correction:* For customer $(i + 1)$, the inter-arrival time is $\text{Arrival}(i + 1) - \text{Arrival}(i)$. If calculating for customer $i$, it should be $\text{Arrival}(i) - \text{Arrival}(i - 1)$.

4. **Slide 77 – Formula 2 (Reversed Subtraction):**
   * *Error:* Stated as $\text{Time customer wait in queue} = \text{Arrival time} - \text{Time service begin}$.
   * *Correction:* Because a customer cannot start service before arriving ($\text{Time service begin} \ge \text{Arrival time}$), this formula produces a negative value or zero. The correct formula is:
     $$\text{Waiting time in queue} = \text{Time service begin} - \text{Arrival time}$$
     *(Note: Slide 79 correctly evaluates $\text{Service Begin} - \text{Arrival Time}$ in practice, contradicting Formula 2 on Slide 77).*

5. **Slide 77 – Item 6 (First Customer Service Begin Time):**
   * *Error:* Stated that for the first customer, service begin is `"zero (always)"`.
   * *Correction:* Service begins upon arrival ($\text{Arrival}_1$). It is only zero if the first customer arrives at clock time $0$. If Customer 1 arrives at $t = 3$, service begins at $t = 3$, not $0$.

6. **Slide 78 – Input Table Row 2 Header:**
   * *Error:* Stated as `"Inter-arrival time (IAT) OR (AT)"`.
   * *Correction:* "AT" stands for Arrival Time (which is already given in row 3 as "Arrival time on clock"), not Inter-arrival Time. Stating "IAT OR AT" conflates interval duration with absolute clock arrival time.
