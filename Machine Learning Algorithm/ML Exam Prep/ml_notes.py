import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from notes_lib import Notes

OUT = r"D:\School-Works\Machine Learning Algorithm"

n = Notes(
    "Machine Learning Reviewer: Modules 1 and 2",
    "CS0075 Machine Learning Algorithm. Built from the Module 1 and Module 2 slides plus the 17 verified formative "
    "questions. Read top to bottom; the blue boxes are memory aids I made (they are not from the slides), and the "
    "red boxes are the traps.",
)

n.h1("How To Use This Reviewer")
n.p("**SA1 covers Module 1 and Module 2 only up to Linear Regression (OLS).** The midterm lecture exam on "
    "**Sat Oct 10** covers all lessons, so the sections are tagged:")
n.table(
    ["Tag", "Meaning", "Where"],
    [
        ["**SA1 + Midterm**", "Covered by SA1 and by the midterm", "Parts 1, 2, and 3.1 to 3.3 (up to Linear Regression)"],
        ["**Midterm only**", "Not in SA1, but expect it on the midterm", "Parts 3.4 onward (Ridge, Lasso, Logistic, Naive Bayes, trees, forests, boosting, SVM)"],
    ],
    [1.5, 2.6, 2.4],
)
n.p("The four parts follow the formative structure: **(1) core concepts, (2) evaluation and complexity, (3) the "
    "algorithms, (4) the traps**. The cram sheet is the last page.")

# ---------------------------------------------------------------- Part 1
n.h1("Part 1. Core Concepts and Definitions   [SA1 + Midterm]")

n.h2("What Machine Learning Is")
n.bullets([
    "Machine learning is about **extracting knowledge from data**. It sits at the intersection of **statistics, "
    "artificial intelligence, and computer science**, and is also known as **predictive analytics** or **statistical learning**.",
    "**Arthur Samuel, 1959**: a field of study concerned with giving computers the ability to **learn without being explicitly programmed**.",
    "ML is a discipline of AI that lets machines **automatically learn from data and past experiences**, identify "
    "patterns, and make **predictions** with **minimal human intervention**.",
])
n.h3("The Formal Definition (E, T, P)")
n.p("A program learns from **experience E** with respect to a class of **tasks T** and **performance measure P** if its "
    "performance at T, as measured by P, **improves with experience E**.")
n.memory("**E**xperience, **T**ask, **P**erformance. Mnemonic: **E**very **T**ry **P**ays off (more experience, better score).")

n.h3("Rule-Based Algorithm vs Machine Learning")
n.table(
    ["", "Traditional Rule-Based Algorithm", "Machine Learning"],
    [
        ["**What drives it**", "A **condition** (rules a person writes)", "**Data** (or experience)"],
        ["**What goes in**", "Rules + data", "Data + answers"],
        ["**What comes out**", "Answers", "The rules (the model)"],
    ],
    [1.5, 2.5, 2.5],
)
n.memory("Rule-based: **R**ules in, **A**nswers out. ML flips it: **D**ata and answers in, the **R**ules out.\n"
         "Fill-in-the-blank: \"Rule-based is Condition. Machine learning is **Data**.\"")

n.h2("Why Machine Learning")
n.bullets([
    "Computers operate **autonomously without explicit programming**; fed new data they learn, grow, and adapt.",
    "Performance **adaptively improves as the number of available samples increases**.",
    "Machines work **24/7**, need no breaks, cost much less to maintain than a human in the long run, and suit tasks that are **routine, repetitive, or tedious**.",
    "Automation also **mitigates risks caused by fatigue or inattention**. Examples in the slides: self-driving cars and robotic arms on production lines.",
])

n.h2("Types of Machine Learning and the Workflow")
n.p("Three learning types: **Supervised, Unsupervised, Reinforcement**. The workflow has two phases:")
n.table(
    ["Phase", "Steps"],
    [
        ["**Phase 1: Learning**", "Training data, **preprocessing** (clean data, format data), **learning** (supervised, unsupervised, reinforcement), **testing** (measure performance, test algorithm)"],
        ["**Phase 2: Prediction**", "**New data** goes into the **trained model**, which outputs **predicted data**"],
    ],
    [1.8, 4.7],
)

n.h2("Python Tools for ML")
n.table(
    ["Name", "What The Slide Says"],
    [
        ["**Scikit-learn**", "The most prominent Python library for ML"],
        ["**NumPy**", "A fundamental package for scientific computing"],
        ["**SciPy**", "A collection of functions for scientific computing"],
        ["**Matplotlib**", "The primary scientific plotting library"],
        ["**Pandas**", "A library for data wrangling and analysis"],
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
n.table(
    ["Category", "Techniques"],
    [
        ["**Data Cleansing**", "Identify and sort out **missing data**, reduce **noisy data**, identify and remove **duplicates**"],
        ["**Feature Engineering**", "**Feature scaling or normalization**, **data reduction**, **discretization**, **feature encoding**"],
    ],
    [1.8, 4.7],
)

n.h2("Exploratory Data Analysis (EDA)")
n.p("EDA understands the main characteristics of the data, spots patterns and **anomalies**, tests a hypothesis, or "
    "checks assumptions, often with visualization.")
n.table(
    ["Activity", "What It Does"],
    [
        ["**Visualization**", "Plots and charts of distributions and relationships"],
        ["**Summary Statistics**", "Mean, median, variance, standard deviation"],
        ["**Outlier Detection**", "Identifying **unusual data points**"],
        ["**Correlation Analysis**", "Examining relationships between variables"],
        ["**Hypothesis Testing**", "Testing initial assumptions about the data"],
    ],
    [2.0, 4.5],
)
n.memory("An **outlier** is the point; **outlier detection** is the process. If the blank says \"identifies unusual data points\", answer the process.")

n.h2("Discrete vs Continuous Data")
n.table(
    ["Type", "Meaning", "Example"],
    [
        ["**Discrete**", "Countable in whole units; you cannot have a fraction of it", "Number of students in a class"],
        ["**Continuous**", "Lies on an unbroken scale", "Height, weight, temperature"],
    ],
    [1.3, 3.4, 1.8],
)
n.memory("**Discrete = Digits you can count.** **Continuous = Can slide** anywhere on the scale.")

n.h2("Model Deployment and Data Ethics (Module 1, Subtopic 2)")
n.p("**Deployment** means taking a trained model and making it available in real applications. The stages are "
    "**Training, Validation, Deployment, Monitoring** (models can **drift** as real-world data evolves). Best practices: "
    "**(1) choose the right infrastructure, (2) effective versioning and tracking, (3) robust testing and validation, "
    "(4) implement monitoring and alerting.**")
n.table(
    ["Data Ethics Principle", "Meaning"],
    [
        ["**Ownership**", "An individual owns their personal information; collecting it without consent is unethical"],
        ["**Transparency**", "Data subjects have a right to know how it is collected, stored, and used"],
        ["**Privacy**", "Protect personally identifiable information (PII) such as full name, birthdate, phone number, bank account number, street address"],
        ["**Intention**", "Ask why you need the data and what you will gain; malicious intent is unethical"],
        ["**Outcomes**", "Even good intentions can cause harm; unintended harm to a group is called **disparate impact**"],
    ],
    [1.8, 4.7],
)
n.memory("**O**wn it, **T**ell them, **P**rotect it, **I**ntend well, check **O**utcomes: **O**ur **T**eam **P**rotects **I**ndividuals' **O**wnership.")

# ---------------------------------------------------------------- Part 2
n.h1("Part 2. Evaluation, Generalization and Complexity   [SA1 + Midterm]")

n.h2("Supervised Learning Basics")
n.bullets([
    "**Labeled training data** has both the **input** and the **correct output** (a label). Each example is a pair: an input object (feature vector) and a desired output value.",
    "The primary objective is to **map the input variable to the output variable**.",
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
n.watch("**Formative Q17 conflict.** The slide says regression \"**predicts consecutive numbers (real numbers)**\", so the "
        "slide-literal answer to \"Regression predicts consecutive numbers\" is **True**. The Gemini key marked it **False** "
        "(regression predicts continuous values, not a counting sequence like 1, 2, 3). Check which one your own formative "
        "feedback accepted before the exam. Rule of thumb: on a quiz copied from these slides, follow the slide wording.")

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

n.h2("Model Complexity")
n.bullets([
    "The more complex the model, the better it predicts the **training** data. Too complex, and it focuses on each individual point and **does not generalize**.",
    "There is a **sweet spot** in between that gives the **best generalization**. That is the model we want.",
    "The larger the **variety** of data points, the more complex a model you can use without overfitting. **Duplicating the same points or collecting very similar data does not help.**",
    "\"Never underestimate the power of **more data**.\"",
])
n.table(
    ["Complexity", "Fit Problem", "Error Type (Slide Definition)"],
    [
        ["**Too low** (too simple)", "**Underfitting**", "**Bias** = error from wrong or too-simple assumptions in the algorithm"],
        ["**Too high** (too flexible)", "**Overfitting**", "**Variance** = error from sensitivity to noise and fluctuations in the training data"],
    ],
    [1.8, 1.6, 3.1],
)
n.watch("\"Low complexity is overfitting\" is **False**. Low complexity is **underfitting**.")
n.p("The boat example: a rule that is 100 percent accurate on 12 rows is not trustworthy. If 10,000 more rows obeyed the "
    "same rule, you would believe it. More data supports a more complex model.")

n.h2("R-Squared (R2, Coefficient of Determination)")
n.table(
    ["Situation", "R2"],
    [
        ["**Perfect prediction** (prediction equals target)", "**1**"],
        ["**Constant model** that always predicts the mean of the training targets (y_train)", "**0**"],
        ["**Worse than predicting the average**", "**Negative**"],
    ],
    [4.6, 1.9],
)
n.memory("R2 is a **report card against guessing the average**: 1 is perfect, 0 is no better than the average, **below 0 is worse than the average**.")
n.watch("The slide also says R2 \"yields a score between 0 and 1\", but the next slide says it **can be negative**. "
        "\"Predicting worse than the average can give a negative number\" is **True** (formative Q11). "
        "For regressors, scikit-learn's **score()** returns **R2**; for classifiers it returns **accuracy**.")

# ---------------------------------------------------------------- Part 3
n.h1("Part 3. The Algorithms")

n.h2("3.1 k-Nearest Neighbors (k-NN)   [SA1 + Midterm]")
n.bullets([
    "Arguably the **simplest** ML algorithm. **Building the model is only storing the training dataset.**",
    "To predict, it finds the **closest training points** (the nearest neighbors).",
    "**Classification:** with k = 1, the prediction is the label of the single nearest point. With k > 1 it uses **voting**: the **majority class** among the k neighbors wins. Works for any number of classes.",
    "**Regression:** with k = 1, the prediction is the target of the nearest neighbor. With k > 1 the prediction is the **average (mean)** of the neighbors.",
    "In scikit-learn: **KNeighborsClassifier** and **KNeighborsRegressor**; train with **fit**, predict with **predict**, evaluate with **score**.",
])
n.table(
    ["", "Small k (for example 1)", "Large k"],
    [
        ["**Decision boundary**", "Jagged; predictions go through every point (**unsteady**)", "**Smoother**; does not fit the training data as well"],
        ["**Model complexity**", "**More complex**", "**Less complex**"],
        ["**Risk**", "**Overfitting** (high variance)", "**Underfitting** (high bias)"],
    ],
    [1.7, 2.5, 2.3],
)
n.memory("**Small k = Small crowd = Super complex = Overfit.** **Big k = Big crowd = Blurry average = Underfit.** "
         "On the accuracy plot, **the best performance is somewhere in the middle**.")
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

n.h2("3.2 Linear Models   [SA1 + Midterm]")
n.bullets([
    "Linear models make a prediction using a **linear function of the input features**: a **best-fit line**.",
    "They assume a **linear relationship** between the outcome and each predictor. Examples: boiling point vs altitude, advertising spend vs revenue, fertilizer vs crop yield.",
    "Types: **Linear Regression** (regression, numeric output) and **Logistic Regression** (classification).",
])
n.h3("The Prediction Formula")
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

n.h2("3.3 Linear Regression (Ordinary Least Squares)   [SA1 + Midterm]")
n.bullets([
    "**Linear regression = ordinary least squares (OLS)**: the simplest and most classic linear method for regression.",
    "It finds **w and b** that **minimize the mean squared error** between predictions and the true targets on the **training set**.",
    "The **mean squared error** is the sum of squared differences between the predictions and the true values (as the slide words it).",
])
n.table(
    ["Example", "Train R2 vs Test R2", "Diagnosis"],
    [
        ["**Wave dataset** (one feature)", "About **0.66**, and the train and test scores are **very close**", "Likely **underfitting**, not overfitting"],
        ["**Extended Boston Housing** (506 samples, **105 features**)", "**Very accurate on train**, much **worse on test**", "**Overfitting**. Too many features inflate the weights. Try a model that **controls complexity**: Ridge"],
    ],
    [2.2, 2.3, 2.0],
)
n.memory("**Close scores, mediocre = underfit. Big gap, high train = overfit.**")

n.pagebreak()
n.p("**SA1 stops here.** Everything below is **midterm only**.")

n.h2("3.4 Ridge Regression   [Midterm only]")
n.bullets([
    "A linear model for regression with the **same prediction formula as OLS**.",
    "The coefficients are also chosen to be **as small as possible** (close to zero, **but not zero**), so each feature has as little effect as it can while still predicting well.",
    "That constraint is **regularization**: **explicitly restricting a model to avoid overfitting**. Ridge uses **L2 regularization** (squared L2 norm).",
    "**Alpha** controls the strength. **Larger alpha, larger penalty, smaller w.** Default **alpha = 1.0**.",
])
n.table(
    ["", "Ridge vs LinearRegression (Boston)"],
    [
        ["**Training score**", "Ridge is **lower**"],
        ["**Test score**", "Ridge is **higher** (less overfitting; Ridge is a more restricted model)"],
        ["**More training data**", "The gap closes; with enough data **regularization matters less**. OLS at tiny sizes could even score **R2 below 0**"],
    ],
    [1.8, 4.7],
)
n.memory("**A**lpha up, **A**ll weights shrink toward zero. A bigger alpha is a **bigger fine**.")
n.watch("\"In Ridge, a larger alpha makes the penalty lesser\" is **False** (formative Q13). Ridge weights **approach zero but never reach it**.")

n.h2("3.5 Lasso   [Midterm only]")
n.bullets([
    "An alternative to Ridge. It also keeps coefficients near zero, but with **L1 regularization**.",
    "Consequence: **some coefficients become exactly zero**, so some features are **ignored entirely**.",
    "Larger alpha again means a larger penalty. **Alpha = 1.0 was too much regularization: underfitting**, using only **4 of the 105 features**. **Lowering alpha** to reduce underfitting used **33 of 105 features** and did slightly better than Ridge. Very low alpha behaves **like plain linear regression**.",
])
n.table(
    ["", "Ridge", "Lasso"],
    [
        ["**Penalty**", "**L2**", "**L1**"],
        ["**Weights**", "Approach zero, **never exactly zero**", "**Can be exactly zero**"],
        ["**Prefer it when**", "**Generally preferred**", "Only **some of many features matter**, or you want a model that is **easy to analyze and understand**"],
    ],
    [1.5, 2.4, 2.6],
)
n.memory("**L1 = Leaves out features** (zeros). **L2 = Loves them all a little** (shrinks, keeps).")

n.h2("3.6 Logistic Regression and LinearSVC   [Midterm only]")
n.bullets([
    "Linear models for **classification**. For binary classification, the prediction is positive (**+1**) if the formula is **greater than 0** and negative (**-1**) if **less than 0**.",
    "The decision boundary is a **line** (1 feature), a **plane** (2 features), or a **hyperplane** (3 or more).",
    "**Logistic regression** is a classification algorithm despite its name. It gives a **probability between 0 and 1** using the **logistic (sigmoid) function**, and a **threshold** decides the class.",
    "The two common linear classifiers: **LogisticRegression** and **linear SVM (LinearSVC)**.",
    "Regularization parameter **C**: **higher C = less regularization** (fits the training set as well as it can); **low C** pushes **w toward zero**. Default **C = 1** with **L2**; **L1** gives a more **interpretable** model using fewer features.",
])
n.watch("C works **opposite** to alpha: **high C = weak regularization**, **high alpha = strong regularization**.")
n.memory("**C** = **C**ontrol is loose when high. **A**lpha = **A**ccuse harder when high.")

n.h2("3.7 Naive Bayes   [Midterm only]")
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

n.h2("3.8 Decision Trees   [Midterm only]")
n.bullets([
    "Used for **classification and regression**. They learn a **hierarchy of if/else questions** leading to a decision.",
    "The questions are called **tests** (not the test set). The top node is the **root** (the whole dataset); the algorithm picks the **most informative** test about the target. Parts: **root node, node, edge, terminal (leaf) node**.",
    "A prediction finds the region the point falls in and returns the **majority target** (or the single target in a pure leaf).",
    "scikit-learn: **DecisionTreeClassifier** and **DecisionTreeRegressor**. Visualize with **export_graphviz** (a **.dot** file). **Feature importances** show what the tree used.",
    "Tree regression is **not affected by feature scale**, but it is **impossible to extrapolate**: it cannot predict outside the range of the training data.",
])

n.h2("3.9 Ensembles: Random Forest and Gradient Boosting   [Midterm only]")
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

n.h2("3.10 Kernelized Support Vector Machines   [Midterm only]")
n.bullets([
    "An extension of linear SVM for **nonlinear** problems that a hyperplane cannot solve. **SVC** for classification, **SVR** for regression.",
    "**Support vectors** are the points that define the decision boundary. The **kernel trick** gives complex boundaries even with few features.",
    "**gamma** controls the width of the **Gaussian (RBF) kernel**: **small gamma = large radius = many points count as close = simpler**.",
    "**C** limits each point's influence: **small C = very restricted model**.",
    "SVMs are **sensitive to feature scale**. Rescale to **0 to 1 with MinMaxScaler**. On the Breast Cancer data this fixed the overfitting, then **increasing C** reached **97.2 percent**.",
    "Weakness: **slow with many samples (more than about 100,000)**; sensitive to preprocessing and parameters. Parameters: **C, gamma** (RBF), coef (sigmoid), degree (polynomial).",
])

# ---------------------------------------------------------------- Part 4
n.h1("Part 4. High-Yield Traps")
n.p("These are the twists the formatives used. Most are a true idea with **one word flipped**.")
n.table(
    ["Trap", "Wrong Idea", "Right Idea"],
    [
        ["Discrete vs continuous", "Number of students is continuous", "**Discrete**: countable whole units"],
        ["Consecutive vs continuous", "Slide wording vs Gemini key", "Slide: regression predicts **consecutive (real) numbers**. Key said **False**. **Check your formative feedback.**"],
        ["Small k", "Small k makes the model less complex", "Small k = **more** complex = overfitting. **False**."],
        ["Low complexity", "Low complexity is overfitting", "Low complexity is **underfitting**. **False**."],
        ["Rule-based vs ML", "ML runs on conditions", "Rule-based = **condition**; ML = **data**"],
        ["Ridge alpha", "Larger alpha makes the penalty lesser", "Larger alpha = **bigger** penalty. **False**."],
        ["Alpha vs C", "High C means strong regularization", "**High C = weak** regularization; high alpha = strong"],
        ["Ridge vs Lasso zeros", "Ridge zeroes out features", "**Lasso** (L1) hits exact zero; **Ridge** (L2) only approaches it"],
        ["Naive Bayes types", "GaussianNB for counts", "Counts = **Multinomial**; continuous = **Gaussian**; binary = **Bernoulli**"],
        ["R2 sign", "R2 can never be negative", "Worse than the mean gives **negative** R2. **True**."],
        ["Offset", "Offset is not the intercept", "Offset = intercept = bias (**b**). **True**."],
        ["Logistic Regression", "A regression algorithm", "A **classification** algorithm despite its name"],
        ["Libraries", "Anaconda or Jupyter is a library", "Libraries: **pandas, SciPy, NumPy** (also scikit-learn, Matplotlib). Anaconda = distribution; Jupyter = environment."],
        ["Outlier word", "Answering the process for the point", "Point = **outlier**; process = **outlier detection**"],
        ["score()", "score() is always accuracy", "**Classifier = accuracy; regressor = R2**"],
    ],
    [1.5, 2.3, 2.7],
)

# ---------------------------------------------------------------- Cram sheet
n.pagebreak()
n.h1("Cram Sheet")
n.p("Everything on one page. **SA1 items first**, midterm-only items after the line.")
n.bullets([
    "**ML** = extracting knowledge from data; learns from **data / experience** to predict with minimal human intervention. **Samuel, 1959**.",
    "**E, T, P**: performance at task T, measured by P, improves with experience E.",
    "**Rule-based** = **condition**; **ML** = **data**.",
    "Workflow: **Learning** (preprocess, learn, test) then **Prediction** (new data into trained model).",
    "**Discrete** = countable. **Continuous** = unbroken scale. **Outlier** = far from average; finding it = **outlier detection** (EDA).",
    "Libraries: **pandas, SciPy, NumPy**, scikit-learn, Matplotlib. Anaconda = distribution, Jupyter = environment.",
    "Preprocessing: **cleansing** (missing, noise, duplicates) and **feature engineering** (scaling, reduction, discretization, encoding).",
    "**Classification** = categorical target. **Regression** = continuous target (slide: consecutive real numbers).",
    "**Generalization** = good on unseen data. **Underfitting** = too simple, **high bias**, poor everywhere. **Overfitting** = memorized training, **high variance**.",
    "**Small k** = complex = overfit. **Large k** = simple = underfit. k-NN: store data, vote (class) or average (regression), Euclidean by default.",
    "**R2**: 1 perfect, 0 = predicts the mean, **negative = worse than the mean**.",
    "**y-hat = w*x + b**; **b** = intercept = offset = bias. **OLS** minimizes mean squared error on the training set.",
    "OLS: small gap and mediocre score = underfit; huge train-test gap (105 features) = overfit.",
    "---- SA1 ends at linear regression. Midterm-only below. ----",
    "**Ridge** = L2, weights shrink but never zero; **larger alpha = larger penalty**. **Lasso** = L1, some weights **exactly zero**.",
    "**Logistic Regression** = classification (sigmoid, threshold). **C high = less regularization**.",
    "**Naive Bayes**: each feature alone, per-class stats. **Gaussian** continuous, **Multinomial** counts, **Bernoulli** binary.",
    "**Decision tree** = if/else tests, cannot extrapolate. **Random forest** = average of independent bootstrapped trees. **Gradient boosting** = shallow trees fixing the previous error, learning rate 0.1.",
    "**SVM** = kernel trick for nonlinear data; **scale to 0-1**; small gamma = simpler; small C = restricted.",
])

if __name__ == "__main__":
    path = os.path.join(OUT, "PAMESA - ML Reviewer.docx")
    print(n.save(path))
