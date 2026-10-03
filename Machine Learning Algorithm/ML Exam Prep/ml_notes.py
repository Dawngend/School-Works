"""Builds the ML reviewers. Usage: python ml_notes.py sa1   or   python ml_notes.py midterm"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from notes_lib import Notes

OUT = r"D:\School-Works\Machine Learning Algorithm"
MODE = sys.argv[1] if len(sys.argv) > 1 else "midterm"
SA1 = MODE == "sa1"

if SA1:
    title = "Machine Learning Reviewer for SA1"
    sub = ("CS0075 Machine Learning Algorithm, SA1. Covers Module 1 and Module 2 up to Linear Regression (OLS). "
           "Built from the slides, including the picture slides, plus the verified formative questions. The blue boxes "
           "are memory aids I made (they are not from the slides) and the red boxes are the traps.")
else:
    title = "Machine Learning Reviewer for the Midterm"
    sub = ("CS0075 Machine Learning Algorithm, midterm lecture exam (all of Module 1 and Module 2). Built from the "
           "slides, including the picture slides, plus the verified formative questions. The blue boxes are memory "
           "aids I made (they are not from the slides) and the red boxes are the traps.")
n = Notes(title, sub)

n.h1("How To Use This Reviewer")
if SA1:
    n.p("This reviewer stops at **Linear Regression (OLS)**, which is where SA1 stops. The separate midterm reviewer "
        "adds everything after it (Ridge, Lasso, Logistic Regression, Naive Bayes, decision trees, random forest, "
        "gradient boosting, and SVM). Parts: **(1) core concepts, (2) evaluation and complexity, (3) k-NN and linear "
        "models, (4) traps**. The cram sheet is the last page.")
else:
    n.p("The midterm covers **all of Module 1 and Module 2**. Parts: **(1) core concepts, (2) evaluation and "
        "complexity, (3) the algorithms, (4) traps**. Section 3.4 onward is the material SA1 did not cover. The cram "
        "sheet is the last page.")

# ================================================================ PART 1
n.h1("Part 1. Core Concepts and Definitions")

n.h2("What Machine Learning Is")
n.bullets([
    "Machine learning is about **extracting knowledge from data**. It sits at the intersection of **statistics, "
    "artificial intelligence, and computer science**, and is also known as **predictive analytics** or **statistical learning**.",
    "**Arthur Samuel, 1959**: giving computers the ability to **learn without being explicitly programmed**.",
    "ML is a discipline of AI that lets machines **automatically learn from data and past experiences**, identify "
    "patterns, and make **predictions** with **minimal human intervention**.",
])
n.h3("The Formal Definition (E, T, P)")
n.p("A program learns from **experience E** with respect to a class of **tasks T** and **performance measure P** if its "
    "performance at T, as measured by P, **improves with experience E**.")
n.memory("**E**xperience, **T**ask, **P**erformance. **E**very **T**ry **P**ays off: more experience, better score.")

n.h3("AI, ML, Deep Learning, and Data Science")
n.bullets([
    "The slide diagrams nest them: **Artificial Intelligence contains Machine Learning, which contains Deep Learning**.",
    "**Data Science** is collection, preparation, and analysis of data, leveraging AI/ML, research, industry expertise, and statistics to make business decisions.",
    "**AI** is technology for machines to understand, interpret, learn, and make \"intelligent\" decisions, and includes ML among many other fields.",
    "**ML** is algorithms that help machines improve through supervised, unsupervised, and reinforcement learning. It is a **subset of AI** and a **Data Science tool**.",
])

n.h3("Rule-Based Algorithm vs Machine Learning")
n.table(
    ["", "Traditional Rule-Based Algorithm", "Machine Learning"],
    [
        ["**What drives it**", "A **condition** (true goes to Code 1, false goes to Code 2)", "**Training data** goes into the ML algorithm, which produces a **model**"],
        ["**How rules arise**", "**Explicit programming**; the rules can be **manually specified**", "Rules are **automatically learned by machines**"],
        ["**Best when**", "Rules are simple", "Decision-making rules are **complex or difficult to describe**; **samples are used for training**"],
        ["**Prediction**", "Not applicable", "**New data** goes into the model, which outputs a **prediction**"],
    ],
    [1.4, 2.5, 2.6],
)
n.memory("Rule-based: **R**ules in, **A**nswers out. ML flips it: **D**ata and answers in, the **R**ules out.\n"
         "Fill-in-the-blank: \"Rule-based is Condition. Machine learning is **Data**.\"")
n.p("The scenario chart plots **rule complexity** (simple to complex) against **scale of the problem** (small to large):")
n.table(
    ["", "Small Scale", "Large Scale"],
    [
        ["**Complex rules**", "**Manual rules**", "**Machine learning algorithms**"],
        ["**Simple rules**", "**Simple problems**", "**Rule-based algorithms**"],
    ],
    [1.8, 2.3, 2.4],
)

n.h2("Why Machine Learning")
n.bullets([
    "Computers operate **autonomously without explicit programming**; fed new data they learn, grow, and adapt.",
    "Performance **adaptively improves as the number of available samples increases**.",
    "Machines work **24/7**, need no breaks, cost much less to maintain than a human in the long run, and suit tasks that are **routine, repetitive, or tedious**.",
    "Automation also **mitigates risks caused by fatigue or inattention**. Slide examples: self-driving cars and robotic arms on production lines.",
    "Application areas on the slides: healthcare, automobile, transportation, manufacturing, e-commerce, insurance; medical diagnosis, image and speech recognition, fraud detection, recommendations, spam filtering, self-driving cars, traffic prediction, stock market trading.",
])

n.h2("Types of Machine Learning and the Workflow")
n.p("The types-of-ML picture shows **four**: **Supervised, Unsupervised, Semi-Supervised, and Reinforcement Learning**. "
    "The \"How does ML work\" text lists three under Learning (supervised, unsupervised, reinforcement).")
n.table(
    ["Phase", "Steps"],
    [
        ["**Phase 1: Learning**", "Training data, **preprocessing** (clean data, format data), **learning**, **testing** (measure performance, test algorithm)"],
        ["**Phase 2: Prediction**", "**New data** goes into the **trained model**, which outputs **predicted data**"],
    ],
    [1.8, 4.7],
)
n.p("In the picture, the training data trains the ML algorithm, then **accuracy** is checked: **unacceptable** sends you "
    "back to train again, **acceptable** gives a **successful model**.")
n.h3("The Four-Stage ML Workflow (DataCamp Slide)")
n.table(
    ["Stage", "Steps"],
    [
        ["**1. Project setup**", "Understand the business goals; choose the solution to your problem"],
        ["**2. Data preparation**", "Data collection, **data cleaning**, **feature engineering**, **split the data**"],
        ["**3. Modeling**", "Hyperparameter tuning, **train your models**, **make predictions**, **assess model performance** (a repeating cycle)"],
        ["**4. Deployment**", "Deploy the model, **monitor** model performance, **improve** your model"],
    ],
    [1.8, 4.7],
)
n.memory("**S**et up, **P**repare, **M**odel, **D**eploy: **S**ome **P**eople **M**ake **D**inner.")

n.h2("Programming Languages and Python Tools")
n.bullets([
    "The top programming languages for ML, in rank order: **1 Python, 2 R, 3 Java, 4 Julia, 5 Scala, 6 C++, 7 JavaScript, 8 Lisp, 9 Haskell, 10 Go**.",
    "**Why Python:** easy-to-read syntax, extensive libraries and frameworks, strong community support, flexibility, compatibility with other languages, scalability and performance.",
])
n.table(
    ["Name", "What The Slide Says"],
    [
        ["**Scikit-learn**", "The most prominent Python library for ML"],
        ["**NumPy**", "A fundamental package for scientific computing (mathematical functions)"],
        ["**SciPy**", "A collection of functions for scientific computing"],
        ["**Matplotlib**", "The primary scientific plotting library (data visualizations)"],
        ["**Seaborn**", "Data visualizations"],
        ["**Pandas**", "A library for data wrangling and analysis (data analysis and manipulation)"],
        ["**TensorFlow**", "Machine learning"],
        ["**Keras**", "Deep learning"],
        ["**PyTorch**", "Machine learning"],
        ["**Scrapy**", "Web crawling"],
        ["**SQLModel**", "Interacts with SQL databases"],
        ["**Anaconda**", "A Python distribution for large-scale data processing, predictive analysis, and scientific computing"],
        ["**Jupyter Notebook**", "An interactive environment for running code in the browser"],
    ],
    [1.8, 4.7],
)
n.watch("Formative Q5 (\"most popular libraries, choose all\") keyed **PANDAS, SCIPY, NUMPY**. Anaconda is a **distribution** and "
        "Jupyter is an **interactive environment**, so they are not libraries. SQL is a query language.")

n.h2("Data Preprocessing")
n.p("Real data has three quality problems: **incompleteness** (missing values or attributes), **noise** (incorrect "
    "records or exceptions), and **inconsistency** (inconsistent records). \"**Without good data, there is no good model.**\" "
    "Preprocessing (also called data preparation) is cleaning, altering, and reorganizing raw data before analysis.")
n.p("A data scientist's time (pie chart): **60 percent data cleaning and organization**, 19 percent data set "
    "collection, 9 percent data mining, 4 percent algorithm improvements, 3 percent training set creation, 5 percent other.")
n.h3("Errors The Slide Marks In A Messy Table")
n.table(
    ["Error", "Example Meaning"],
    [
        ["**Missing value**", "A blank cell"],
        ["**Invalid value**", "A value outside what is allowed (for example a letter in a gender column that expects M or F)"],
        ["**Invalid duplicate item**", "The same Id appears twice"],
        ["**Value in another column**", "A value that should be in a different column"],
        ["**Misspelling**", "For example \"Ytali\" for Italy"],
        ["**Incorrect format**", "A date written in a different format"],
        ["**Attribute dependency**", "Columns whose values contradict each other"],
    ],
    [2.2, 4.3],
)
n.h3("Key Steps in Order")
n.p("**Data profiling, data cleansing, data reduction, data transformation, data enrichment, data validation.**")
n.table(
    ["Category", "Techniques"],
    [
        ["**Data Cleansing**", "Identify and sort out **missing data**, reduce **noisy data**, identify and remove **duplicates**"],
        ["**Feature Engineering**", "**Feature scaling or normalization**, **data reduction**, **discretization**, **feature encoding**"],
    ],
    [1.8, 4.7],
)
n.h3("Outliers")
n.p("An **outlier** is an observation that seems to be **distant from other observations** or, more specifically, one "
    "observation that **follows a different logic or generative process** than the other observations. **A single "
    "outlier can throw off a regression estimate** (the regression line gets pulled toward it).")

n.h2("Exploratory Data Analysis (EDA)")
n.p("EDA understands the main characteristics of the data, spots patterns and **anomalies**, tests a hypothesis, or "
    "checks assumptions, often with visualization.")
n.table(
    ["Activity", "What It Does"],
    [
        ["**Visualization**", "Plots and charts of distributions and relationships. **Bar plots and histograms** visualize the **count** of values"],
        ["**Summary Statistics**", "Mean, median, variance, standard deviation"],
        ["**Outlier Detection**", "Identifying **unusual data points**"],
        ["**Correlation Analysis**", "Examining relationships between variables"],
        ["**Hypothesis Testing**", "Testing initial assumptions about the data"],
    ],
    [2.0, 4.5],
)
n.memory("The point is the **outlier**; the process is **outlier detection**. \"Identifies unusual data points\" means the process.")
n.h3("The Titanic Example Used In The Slides")
n.bullets([
    "**Titanic Survival Data Set**: 1309 passengers and whether they survived; the goal is to **predict survival from the attributes**. Tabular data can have **different data types in one table**.",
    "Types: **Survived** is integer binary (the **label**); **Pclass** is integer categorical or ordinal; **Name** and **Ticket** are strings; **Sex** and **Embarked** are string categorical; **Age** and **Fare** are continuous; **SibSp** and **Parch** are non-negative integers.",
    "**Feature selection**: dropping columns that are not useful (for example Name, Ticket, Cabin).",
    "**Missing values**: Age had **177** missing values and Embarked had **2**. Two options: **remove rows** with missing values, or **imputation** (filling in missing values by estimating them).",
    "**Mean imputation** (for a numeric column) and **most-frequent imputation** (mode, for a categorical column). Other imputers: median, iterative, kNN.",
    "**Column transformation** before training: **standard scaling** for numerical data (Age, Fare), **ordinal encoding** for categorical data (Pclass, Sex, Embarked); other features are retained.",
])

n.h2("Discrete vs Continuous Data")
n.table(
    ["Type", "Meaning", "Example"],
    [
        ["**Discrete**", "Countable in whole units; you cannot have a fraction of it", "Number of students in a class"],
        ["**Continuous**", "Lies on an unbroken scale", "Height, weight, temperature, Age, Fare"],
    ],
    [1.3, 3.4, 1.8],
)
n.memory("**Discrete = Digits you can count.** **Continuous = Can slide** anywhere on the scale.")

n.h2("Model Deployment")
n.p("**Deployment** means taking a trained model and making it available in real applications. The stages are "
    "**Training, Validation, Deployment, Monitoring** (models can **drift** as real-world data evolves). Deployment "
    "means defining real-time data handling, storage, predictions, APIs and tools, hardware (cloud or on-prem), and a "
    "pipeline for continuous training. Best practices: **(1) choose the right infrastructure, (2) effective versioning "
    "and tracking, (3) robust testing and validation, (4) implement monitoring and alerting.**")

n.h2("Ethics and Privacy in Data Science")
n.table(
    ["Five Principles", "Meaning"],
    [
        ["**Ownership**", "An individual owns their personal information; collecting it without consent is unethical"],
        ["**Transparency**", "Data subjects have a right to know how it is collected, stored, and used"],
        ["**Privacy**", "Protect personally identifiable information (PII): full name, birthdate, phone number, bank account number, street address"],
        ["**Intention**", "Ask why you need the data and what you will gain; malicious intent is unethical"],
        ["**Outcomes**", "Even good intentions can cause harm; unintended harm to a group is **disparate impact**"],
    ],
    [1.8, 4.7],
)
n.memory("**O**wn it, **T**ell them, **P**rotect it, **I**ntend well, check **O**utcomes: **O**ur **T**eam **P**rotects **I**ndividuals' **O**wnership.")
n.table(
    ["Topic", "What The Slides Say"],
    [
        ["**Three new rules of data**", "**Trust over transactions** (consent); **Insight over identity** (re-think transferring PII); **Flows over silos** (teams share the flow of insights)"],
        ["**Regulations shown**", "**GDPR** (General Data Protection Regulation) and the **National Privacy Commission** (Philippines)"],
        ["**Data subject rights**", "Right to **be informed**, to **damages**, to **access**, to **erasure or blocking**, to **file a complaint**, to **object**, to **rectify**, and to **data portability**"],
        ["**Data governance**", "A set of principles and processes for data collection, management, and use, so data is **accurate, consistent, and available** while protecting privacy and security. A **framework** describes **how** to do what governance says the organization needs to do"],
        ["**Pillars of data governance**", "Ownership and accountability, data quality, data protection and safety, data use and availability, data management (built on people, processes, and technology)"],
        ["**10 questions before AI in public decisions**", "Objective, use, impacts, assumptions, data, inputs, mitigation, ethics, oversight, evaluation"],
    ],
    [2.0, 4.5],
)

# ================================================================ PART 2
n.h1("Part 2. Evaluation, Generalization and Complexity")

n.h2("Supervised Learning Basics")
n.bullets([
    "**Labeled training data** has both the **input** (data features) and the **correct output** (the label or goal). Each example is a pair: an input object (feature vector) and a desired output value.",
    "The primary objective is to **map the input variable to the output variable**: y = f(x). In the slide example, weather, temperature, and wind speed are the input x and \"Enjoy Sports\" (yes or no) is the output y.",
    "Two phases: **training and validation**, followed by **prediction**.",
])
n.table(
    ["", "Classification", "Regression"],
    [
        ["**Target**", "**Categorical** variable", "**Continuous** variable"],
        ["**Predicts**", "One of the possible **class labels**", "**Consecutive numbers (real numbers)**, per the slide"],
        ["**Examples**", "Spam or not spam, COVID positive or negative on a chest X-ray, handwritten digit recognition", "Stock price forecast, weather prediction, annual income forecast, population forecast"],
        ["**Subtypes**", "**Binary** (two classes) and **multiple** (three or more)", "Simple linear, multivariate"],
        ["**Algorithms (slide)**", "Random Forest, Decision Tree, Logistic Regression, Support Vector Machine", "Simple Linear Regression, Multivariate Regression, Decision Tree, Lasso Regression"],
    ],
    [1.4, 2.6, 2.5],
)
n.watch("**Formative Q17.** The slide says regression \"**predicts consecutive numbers (real numbers)**\". The graded formative key "
        "marked \"Regression predicts consecutive numbers\" as **False** (regression predicts **continuous real values**, not a counting "
        "sequence like 1, 2, 3). Study rule: **regression = continuous real numbers**. If a true or false item says "
        "\"consecutive numbers\" with no mention of real numbers, go with the **formative key (False)**, because your teacher "
        "wrote both the quiz and the exam. If the item says \"real numbers\", it is True.")

n.h2("Generalization, Overfitting, Underfitting")
n.table(
    ["Term", "What The Slides Say", "Train", "Test"],
    [
        ["**Generalization**", "The model makes accurate predictions on **new, unseen data** with the same characteristics as the training set. We want to generalize **as accurately as possible**.", "Good", "Good"],
        ["**Overfitting**", "The model fits the **particularities of the training set** (its noise and outliers) too closely; it has **memorized** the training data rather than learned the pattern.", "Very good", "Poor"],
        ["**Underfitting**", "The model is **too simple** to capture the variability in the data and does badly **even on the training set**.", "Poor", "Poor"],
    ],
    [1.4, 3.3, 0.9, 0.9],
)
n.memory("**Under = Underbuilt** (bad everywhere). **Over = Overthinks** (aces training, flops on new data).")

n.h2("Model Complexity and the Complexity Curve")
n.bullets([
    "The curve plots **accuracy** against **model complexity**. **Training accuracy keeps rising** as complexity rises. "
    "**Generalization (test) accuracy rises, peaks at the sweet spot, then falls.**",
    "**Left side = underfitting** (too simple). **Right side = overfitting** (too complex). The **sweet spot** in between gives the **best generalization**.",
    "The more complex the model, the better it predicts the **training** data. Too complex, and it focuses on each individual point and **does not generalize**.",
    "The larger the **variety** of data points, the more complex a model you can use without overfitting. **Duplicating the same points or collecting very similar data does not help.** \"Never underestimate the power of **more data**.\"",
])
n.table(
    ["Complexity", "Fit Problem", "Error Type (Slide Definition)"],
    [
        ["**Too low** (too simple)", "**Underfitting**", "**Bias** = error from wrong or too-simple assumptions in the algorithm"],
        ["**Too high** (too flexible)", "**Overfitting**", "**Variance** = error from sensitivity to noise and fluctuations in the training data"],
    ],
    [1.8, 1.6, 3.1],
)
n.p("The **dartboard** picture: **low bias and low variance = good model** (darts tightly clustered on the bullseye). "
    "High bias means the cluster is off the bullseye; high variance means the darts are spread out.")
n.watch("\"Low complexity is overfitting\" is **False**. Low complexity is **underfitting**.")
n.p("The boat example: a rule that is 100 percent accurate on 12 rows is not trustworthy. If 10,000 more rows obeyed the "
    "same rule, you would believe it. More data supports a more complex model.")

n.h2("R-Squared (R2, Coefficient of Determination)")
n.p("**R2 = 1 - [sum of (y - y-hat) squared] / [sum of (y - y-bar) squared]**, where **y** is the target value, "
    "**y-bar** the average value, and **y-hat** the predicted value.")
n.table(
    ["Situation", "R2"],
    [
        ["**Perfect prediction** (prediction equals target, numerator equals zero)", "**1**"],
        ["**Predicting the average** (numerator equals denominator): a constant model that predicts the mean of y_train", "**0**"],
        ["**Worse than predicting the average**", "**Negative**"],
    ],
    [4.6, 1.9],
)
n.memory("R2 is a **report card against guessing the average**: 1 is perfect, 0 is no better than the average, **below 0 is worse than the average**.")
n.watch("The slide also says R2 \"yields a score between 0 and 1\", but the next slide says it **can be negative**. "
        "\"Predicting worse than the average can give a negative number\" is **True** (formative Q11). "
        "For regressors, scikit-learn's **score()** returns **R2**; for classifiers it returns **accuracy**.")

# ================================================================ PART 3
n.h1("Part 3. The Algorithms")

n.h2("3.1 k-Nearest Neighbors (k-NN)")
n.bullets([
    "Arguably the **simplest** ML algorithm. **Building the model is only storing the training dataset.**",
    "To predict, it finds the **closest training points** (the nearest neighbors).",
    "**Classification:** with k = 1, the prediction is the label of the single nearest point. With k > 1 it uses **voting**: the **majority class** among the k neighbors wins. Works for any number of classes.",
    "**Regression:** with k = 1, the prediction is the target of the nearest neighbor. With k > 1 the prediction is the **average (mean)** of the neighbors.",
    "In scikit-learn: **KNeighborsClassifier** and **KNeighborsRegressor**; train with **fit**, predict with **predict**, evaluate with **score**.",
])
n.table(
    ["", "Small k (1 neighbor)", "Large k (9 neighbors)"],
    [
        ["**Decision boundary**", "Jagged; predictions go through every point (**unsteady**)", "**Smoother**; does not fit the training data as well"],
        ["**Model complexity**", "**More complex**", "**Less complex**"],
        ["**Bias and variance**", "Bias goes **down**, variance goes **up**", "Bias goes **up**, variance goes **down**"],
        ["**Risk**", "**Overfitting**", "**Underfitting**"],
    ],
    [1.7, 2.5, 2.3],
)
n.p("On the **accuracy against n_neighbors** plot, **training accuracy falls** as n_neighbors grows, test accuracy peaks around "
    "6, and **the best performance is somewhere in the middle** (the optimal point). The left side is overfitting and the right side is underfitting.")
n.memory("**Small k = Small crowd = Super complex = Overfit.** **Big k = Big crowd = Blurry average = Underfit.**")
n.watch("\"A small k makes the model less complex\" is **False** (formative Q9). \"In k-NN, low model complexity is "
        "overfitting\" is **False** (Q10): low complexity is underfitting.")
n.table(
    ["Important Parameters", "Strengths", "Weaknesses"],
    [
        ["**Number of neighbors** and the **distance measure** (**Euclidean** by default). Three or five neighbors usually works well, but adjust it.",
         "Easy to understand; works well **without special adjustments**; suitable as a **first model**",
         "**Slow** prediction when features or samples are many, so preprocessing matters; does **not work well with sparse datasets**"],
    ],
    [2.5, 2.0, 2.0],
)

n.h2("3.2 Linear Models")
n.bullets([
    "Linear models make a prediction using a **linear function of the input features**: a **best-fit line**.",
    "They assume a **linear relationship** between the outcome and each predictor. Examples: boiling point vs altitude, advertising spend vs revenue, fertilizer vs crop yield, athlete performance vs training.",
    "Types: **Linear Regression** (regression, numeric output) and **Logistic Regression** (classification).",
])
n.h3("The Prediction Formula")
n.p("**y-hat = w[0]*x[0] + w[1]*x[1] + ... + w[p]*x[p] + b**")
n.table(
    ["Symbol", "Meaning"],
    [
        ["**x[0] to x[p]**", "The features (**p + 1** of them)"],
        ["**w[0] to w[p]**", "The **weights** or **coefficients** (the slopes)"],
        ["**b**", "The **intercept**, also called the **offset** or **bias**"],
        ["**y-hat**", "The model's prediction"],
    ],
    [1.8, 4.7],
)
n.memory("**w** = **W**eight = slope. **b** = **B**ias = intercept = offset. All three of intercept, offset, and bias point at **b**.")
n.p("In scikit-learn the weights are stored in **coef_** and the intercept in **intercept_**. "
    "\"The offset parameter is also called the intercept\" is **True** (formative Q12).")

n.h2("3.3 Linear Regression (Ordinary Least Squares)")
n.bullets([
    "**Linear regression = ordinary least squares (OLS)**: the simplest and most classic linear method for regression.",
    "It finds **w and b** that **minimize the mean squared error** between predictions and the true targets on the **training set**.",
    "The **mean squared error** is the sum of squared differences between the predictions and the true values (as the slide words it).",
])
n.table(
    ["Example", "Train R2 vs Test R2", "Diagnosis"],
    [
        ["**Wave dataset** (one feature)", "About **0.66**, and the train and test scores are **very close**", "Likely **underfitting**, not overfitting"],
        ["**Extended Boston Housing** (506 samples, **104 or 105 features**)", "**Very accurate on train**, much **worse on test**", "**Overfitting**. Too many features inflate the weights. Try a model that **controls complexity**: Ridge"],
    ],
    [2.2, 2.3, 2.0],
)
n.p("The extended Boston data is the **13 original features plus the 91 two-feature products** (the slide's shape is (506, 104); "
    "the slide text elsewhere says 105 features). Including derived features like these is **feature engineering**.")
n.memory("**Close scores, mediocre = underfit. Big gap, high train = overfit.**")

if SA1:
    n.p("**SA1 stops here.** The midterm reviewer continues with Ridge, Lasso, Logistic Regression, Naive Bayes, decision "
        "trees, random forests, gradient boosting, and SVM.")
else:
    n.pagebreak()
    n.p("**SA1 stopped at the end of 3.3.** Everything from here is the extra material for the midterm.")

    n.h2("3.4 Ridge Regression")
    n.bullets([
        "A linear model for regression with the **same prediction formula as OLS**.",
        "The coefficients are also chosen to be **as small as possible** (close to zero, **but not zero**), so each feature has as little effect as it can while still predicting well.",
        "That constraint is **regularization**: **explicitly restricting a model to avoid overfitting**. Ridge uses **L2 regularization** (the **L2 norm squared**).",
        "**Cost function: MSE + alpha * (sum of w squared).** **Larger alpha, larger penalty, smaller w.** Default **alpha = 1.0**.",
    ])
    n.table(
        ["", "Ridge vs LinearRegression (Boston)"],
        [
            ["**Training score**", "Ridge is **lower** (0.89 in the slide)"],
            ["**Test score**", "Ridge is **higher** (0.75 in the slide); less overfitting because Ridge is a more restricted model"],
            ["**More training data**", "The gap closes; with enough data **regularization matters less**. OLS at tiny sizes could even score **R2 below 0**"],
        ],
        [1.8, 4.7],
    )
    n.memory("**A**lpha up, **A**ll weights shrink toward zero. A bigger alpha is a **bigger fine**.")
    n.watch("\"In Ridge, a larger alpha makes the penalty lesser\" is **False** (formative Q13). Ridge weights **approach zero but never reach it**.")

    n.h2("3.5 Lasso")
    n.bullets([
        "An alternative to Ridge. It also keeps coefficients near zero, but with **L1 regularization** (the L1-norm, a diamond shape in the slide picture).",
        "**Cost function: MSE + alpha * (sum of the absolute values of w).** Consequence: **some coefficients become exactly zero**, so some features are **ignored entirely**.",
        "Alpha = 1.0 (default) was too much regularization: **underfitting**, using only **4 of the 105 features**. **Lowering alpha** used **33 of 105 features** and did slightly better than Ridge.",
        "Alpha = 0.0001 was too low: train 0.95, test 0.64, **96 features used**, so it behaves **like linear regression**.",
    ])
    n.table(
        ["", "Ridge", "Lasso"],
        [
            ["**Penalty**", "**L2** (squared weights)", "**L1** (absolute weights)"],
            ["**Weights**", "Approach zero, **never exactly zero**", "**Can be exactly zero**"],
            ["**Prefer it when**", "**Generally preferred** (L2 over L1)", "Only **some of many features matter**, or you want a model that is **easy to analyze and understand**"],
        ],
        [1.5, 2.4, 2.6],
    )
    n.memory("**L1 = Leaves out features** (zeros). **L2 = Loves them all a little** (shrinks, keeps).")

    n.h2("3.6 Logistic Regression and LinearSVC")
    n.bullets([
        "Linear models for **classification**. For binary classification, the prediction is positive (**+1**) if the formula is **greater than 0** and negative (**-1**) if **less than 0**; y-hat is the **decision boundary**.",
        "The boundary is a **line** (1 feature), a **plane** (2 features), and a **hyperplane** (3 or more).",
        "Classification in linear models depends on how well the weights and intercept fit the training data, the **cost or loss function**, and **regularization**.",
        "**Logistic regression** is a classification algorithm despite its name. It gives a **probability between 0 and 1** using the **logistic (sigmoid) function**, and a **threshold** decides the class.",
        "The two common linear classifiers: **LogisticRegression** and **linear SVM (LinearSVC)**.",
        "Regularization parameter **C**: **higher C = less regularization** (fits the training set as well as it can); **low C** pushes **w toward zero**. Default **C = 1** with **L2**. On the cancer data, C = 1 gave 94 percent on both train and test (likely underfitting); **L1** gives a more **interpretable** model using fewer features.",
    ])
    n.watch("C works **opposite** to alpha: **high C = weak regularization**, **high alpha = strong regularization**.")
    n.memory("**C** = **C**ontrol is loose when high. **A**lpha = **A**ccuse harder when high.")

    n.h2("3.7 Naive Bayes")
    n.bullets([
        "A family of classifiers quite similar to linear models; **training is faster** than a linear classifier, with slightly lower generalization.",
        "They are efficient because they learn parameters by looking at **each feature individually** and collecting **simple per-class statistics** from each feature (formative Q15: **True**).",
        "**Alpha** controls model complexity by smoothing statistics. **Larger alpha decreases complexity** but does not change performance much.",
        "Works well with **sparse, high-dimensional** data and is **not parameter sensitive**. Training and prediction are fast and easy to understand.",
    ])
    n.table(
        ["Classifier", "Data"],
        [
            ["**GaussianNB**", "**Continuous** data"],
            ["**BernoulliNB**", "**Binary** data, text data"],
            ["**MultinomialNB**", "**Integer count** data, text data"],
        ],
        [2.0, 4.5],
    )
    n.memory("**G**aussian = **G**rades on a scale (continuous). **B**ernoulli = **B**inary. **M**ultinomial = **M**any counts.")

    n.h2("3.8 Decision Trees")
    n.bullets([
        "Used for **classification and regression**. They learn a **hierarchy of if/else questions** leading to a decision.",
        "In the animal tree picture: the top node is the **root node** (\"Has feathers?\"), the questions are the **nodes** (characteristics: \"Can fly?\", \"Has fins?\"), the arrows are **edges** (true or false), and the answers (Hawk, Penguin, Dolphin, Bear) are **terminal nodes** (leaves).",
        "The questions are called **tests** (not the test set). The algorithm picks the **most informative** test about the target. For continuous data a test looks like \"Is feature greater than a?\". The root represents the whole dataset.",
        "A prediction finds the region the point falls in by going left or right from the root, then returns the **majority target** (or the single target in a pure leaf).",
        "scikit-learn: **DecisionTreeClassifier** and **DecisionTreeRegressor**. Visualize with **export_graphviz** (a **.dot** file). **Feature importances** show what the tree used.",
        "Tree regression is **not affected by feature scale**, but it **cannot extrapolate**: on the RAM price data its prediction stays **flat** after the training range, while the linear model keeps following the trend.",
    ])

    n.h2("3.9 Ensembles: Random Forest and Gradient Boosting")
    n.p("**Ensembles combine multiple models** into a more powerful one. Both below use **decision trees** as building blocks.")
    n.table(
        ["", "Random Forest", "Gradient Boosting"],
        [
            ["**Idea**", "**Reduces overfitting by averaging** many trees; **injects randomness**", "Each new tree **compensates for the error of the previous tree**"],
            ["**Trees**", "Built **independently**; each from a **bootstrap sample** (draw with replacement; about **one third** of points missing)", "**Shallow** trees, depth **5 or less**; **pre-pruning** is applied, not randomness"],
            ["**Prediction**", "Regression: **average of values**. Classification: **average of predicted probabilities**", "Regression: **least squares** loss. Classification: **logistic** loss. Uses **gradient descent**"],
            ["**Key parameters**", "**n_estimators**, **max_features**", "**n_estimators**, **learning_rate** (default **0.1**), **max_depth**"],
            ["**Strengths**", "Widely used; excellent performance; little tuning; **no scaling needed**", "Slightly **better than random forest**; no scaling needed"],
            ["**Weaknesses**", "Hard to analyze; poor on **large sparse** data; **more memory and slower** than linear models", "**Sensitive to parameters**; longer training; poor on sparse high-dimensional data"],
        ],
        [1.2, 2.7, 2.6],
    )
    n.memory("**Forest = many independent trees VOTE (average).** **Boosting = trees take TURNS fixing the last one's mistakes.**")
    n.p("On the Breast Cancer data: random forest gave **97 percent** with no tuning; gradient boosting at defaults hit "
        "**100 percent on training**, a sign of **overfitting**, fixed by **limiting depth** or **lowering the learning rate**.")

    n.h2("3.10 Kernelized Support Vector Machines")
    n.bullets([
        "An extension of linear SVM for **nonlinear** problems that a hyperplane cannot solve. **SVC** for classification, **SVR** for regression.",
        "**Support vectors** are the points that define the decision boundary. The **kernel trick** gives complex boundaries even with few features.",
        "**gamma** controls the width of the **Gaussian (RBF) kernel**: **small gamma = large radius = many points count as close = simpler**.",
        "**C** limits each point's influence: **small C = very restricted model**.",
        "SVMs are **sensitive to feature scale**. Rescale to **0 to 1 with MinMaxScaler**. On the Breast Cancer data this fixed the overfitting, then **increasing C** reached **97.2 percent**.",
        "Weakness: **slow with many samples (more than about 100,000)**; sensitive to preprocessing and parameters. Parameters: **C, gamma** (RBF), coef (sigmoid), degree (polynomial).",
    ])

# ================================================================ PART 4
n.h1("Part 4. High-Yield Traps")
n.p("These are the twists the formatives used, plus the slide details most likely to be tested. Most are a true idea "
    "with **one word flipped**.")
traps = [
    ["Discrete vs continuous", "Number of students is continuous", "**Discrete**: countable whole units", True],
    ["Consecutive vs continuous", "Regression predicts counting numbers", "Regression = **continuous real numbers**. Formative key: \"consecutive numbers\" is **False**", True],
    ["Small k", "Small k makes the model less complex", "Small k = **more** complex = overfitting. **False**.", True],
    ["Low complexity", "Low complexity is overfitting", "Low complexity is **underfitting**. **False**.", True],
    ["Rule-based vs ML", "ML runs on conditions", "Rule-based = **condition**; ML = **data**", True],
    ["Types of ML", "There are three types", "The picture shows **four**: supervised, unsupervised, **semi-supervised**, reinforcement", True],
    ["Libraries", "Anaconda or Jupyter is a library", "Libraries: **pandas, SciPy, NumPy**, etc. Anaconda = distribution; Jupyter = environment", True],
    ["Outlier word", "Answering the process for the point", "Point = **outlier**; process = **outlier detection**", True],
    ["Missing values", "Only one way to handle them", "**Remove rows** or **impute** (mean for numeric, most frequent for categorical)", True],
    ["Python's rank", "Java is the top ML language", "**Python is 1**, R is 2, Java is 3", True],
    ["R2 sign", "R2 can never be negative", "Worse than the mean gives **negative** R2. **True**.", True],
    ["Offset", "Offset is not the intercept", "Offset = intercept = bias (**b**). **True**.", True],
    ["score()", "score() is always accuracy", "**Classifier = accuracy; regressor = R2**", True],
    ["Ridge alpha", "Larger alpha makes the penalty lesser", "Larger alpha = **bigger** penalty. **False**.", False],
    ["Alpha vs C", "High C means strong regularization", "**High C = weak** regularization; high alpha = strong", False],
    ["Ridge vs Lasso zeros", "Ridge zeroes out features", "**Lasso** (L1) hits exact zero; **Ridge** (L2) only approaches it", False],
    ["Naive Bayes types", "GaussianNB for counts", "Counts = **Multinomial**; continuous = **Gaussian**; binary = **Bernoulli**", False],
    ["Logistic Regression", "A regression algorithm", "A **classification** algorithm despite its name", False],
    ["Trees and scale", "Trees need scaled features", "Trees and forests **do not need scaling**; SVM and k-NN do", False],
    ["Forest vs boosting", "Both build trees independently", "Forest = **independent** trees averaged; boosting = trees built **in turn**, each fixing the last", False],
]
n.table(
    ["Trap", "Wrong Idea", "Right Idea"],
    [t[:3] for t in traps if t[3] or not SA1],
    [1.5, 2.3, 2.7],
)

# ================================================================ Cram sheet
n.pagebreak()
n.h1("Cram Sheet")
n.p("Everything on one page." + ("" if SA1 else " **SA1 items first**, midterm-only items after the line."))
n.bullets([
    "**ML** = extracting knowledge from data; learns from **data / experience** to predict with minimal human intervention. **Samuel, 1959**. **AI contains ML contains Deep Learning**.",
    "**E, T, P**: performance at task T, measured by P, improves with experience E.",
    "**Rule-based** = **condition**, manually specified rules; **ML** = **data**, rules learned automatically.",
    "**Four types** (picture): supervised, unsupervised, **semi-supervised**, reinforcement. Workflow: **project setup, data preparation, modeling, deployment**.",
    "Python is **#1** (then R, Java). Libraries: **pandas, NumPy, SciPy, Matplotlib, Seaborn**, scikit-learn, TensorFlow, Keras, PyTorch.",
    "Data problems: **incompleteness, noise, inconsistency**. Preprocessing steps: **profiling, cleansing, reduction, transformation, enrichment, validation**. Data scientists spend **60 percent** on cleaning.",
    "**Outlier** = far from the rest; **outlier detection** = EDA process. Missing values: **remove rows or impute** (mean, most frequent).",
    "**Discrete** = countable. **Continuous** = unbroken scale. **Classification** = categorical target. **Regression** = continuous target.",
    "**Generalization** = good on unseen data. **Underfitting** = too simple, **high bias**. **Overfitting** = memorized training, **high variance**. **Low bias + low variance = good model**.",
    "**Small k** = complex = overfit. **Large k** = simple = underfit. k-NN: store data, vote (class) or average (regression), Euclidean by default.",
    "**R2** = 1 - SS_res / SS_tot: 1 perfect, 0 = predicts the mean, **negative = worse than the mean**.",
    "**y-hat = w*x + b**; **b** = intercept = offset = bias. **OLS** minimizes mean squared error on the training set.",
    "OLS: small gap and mediocre score = underfit; huge train-test gap (many features) = overfit.",
])
if not SA1:
    n.bullets([
        "---- SA1 ends at linear regression. Midterm-only below. ----",
        "**Ridge** = L2, cost MSE + alpha*sum(w squared), never exactly zero; **larger alpha = larger penalty**. **Lasso** = L1, some weights **exactly zero**.",
        "**Logistic Regression** = classification (sigmoid, threshold). **C high = less regularization**.",
        "**Naive Bayes**: each feature alone, per-class stats. **Gaussian** continuous, **Multinomial** counts, **Bernoulli** binary.",
        "**Decision tree** = if/else tests, cannot extrapolate. **Random forest** = average of independent bootstrapped trees. **Gradient boosting** = shallow trees fixing the previous error, learning rate 0.1.",
        "**SVM** = kernel trick for nonlinear data; **scale to 0-1**; small gamma = simpler; small C = restricted.",
    ])

if __name__ == "__main__":
    name = "PAMESA - ML SA1 Reviewer" if SA1 else "PAMESA - ML Midterm Reviewer"
    print(n.save(os.path.join(OUT, name + ".docx")))
