"""Builds AndyHub notes (new layout) for the ML SA1 and midterm reviewers -> andyhub_ml_notes.json"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ml_code_blocks import IMPORT_ROWS, NOTEBOOK, SLIDES
from ml_100_items import CODE, IMPORTS
REFS = ["M1-MAIN-1.pdf", "M2 - Supervised Learning - Main.pdf"]


def sec(heading, summary, aids=(), tables=()):
    return {
        "heading": heading,
        "summary": summary,
        "key_terms": [],
        "properties": [],
        "worked_examples": [],
        "common_mistakes": [],
        "source_refs": REFS,
        "memory_aids": [{"label": l, "text": t} for l, t in aids],
        "comparisons": [{"title": t, "columns": c, "rows": r} for t, c, r in tables],
    }


SA1_SECTIONS = [
    sec("What Machine Learning Is",
        "ML is about extracting knowledge from data. It sits at the intersection of statistics, AI, and computer science, and is "
        "also called predictive analytics or statistical learning. Arthur Samuel (1959): giving computers the ability to learn "
        "without being explicitly programmed. Formal definition: a program learns from experience E on tasks T with "
        "performance measure P if its performance at T, measured by P, improves with E. The slides nest AI > ML > Deep Learning; "
        "ML is a subset of AI and a Data Science tool.",
        [("E, T, P", "Experience, Task, Performance. Every Try Pays off: more experience, better score.")],
        [("AI, ML, Deep Learning, Data Science", ["Term", "What The Slides Say"],
          [["Artificial Intelligence", "Technology for machines to understand, learn, and make intelligent decisions; includes ML"],
           ["Machine Learning", "Algorithms that improve through supervised, unsupervised, and reinforcement learning; subset of AI"],
           ["Deep Learning", "Nested inside ML"],
           ["Data Science", "Collection, preparation, and analysis of data using AI/ML, research, and statistics for business decisions"]])]),
    sec("Rule-Based Algorithm vs Machine Learning",
        "Rule-based algorithms run on a condition (true goes to Code 1, false goes to Code 2) and the rules are manually "
        "specified through explicit programming. Machine learning runs on data: training data goes into the ML algorithm to "
        "make a model, then new data goes into the model for a prediction. Use ML when the decision-making rules are complex "
        "or hard to describe; the rules are learned automatically.",
        [("Flip the inputs", "Rule-based: Rules in, Answers out. ML: Data and answers in, the Rules out. Fill-in-the-blank: rule-based is Condition, ML is Data.")],
        [("Scenario Chart", ["", "Small Scale", "Large Scale"],
          [["Complex rules", "Manual rules", "Machine learning algorithms"], ["Simple rules", "Simple problems", "Rule-based algorithms"]])]),
    sec("Types of ML and the Workflow",
        "The types-of-ML picture shows four: supervised, unsupervised, semi-supervised, and reinforcement learning (the text "
        "lists three under Learning). Phase 1 Learning: training data, preprocessing (clean, format), learning, testing "
        "(measure performance). Phase 2 Prediction: new data into the trained model gives predicted data. If accuracy is "
        "unacceptable, train again; if acceptable, you have a successful model.",
        [("Four stages", "Set up, Prepare, Model, Deploy: Some People Make Dinner.")],
        [("The Four-Stage ML Workflow", ["Stage", "Steps"],
          [["1. Project setup", "Understand the business goals; choose the solution"],
           ["2. Data preparation", "Data collection, data cleaning, feature engineering, split the data"],
           ["3. Modeling", "Hyperparameter tuning, train models, make predictions, assess model performance"],
           ["4. Deployment", "Deploy the model, monitor performance, improve the model"]])]),
    sec("Python Tools and Languages",
        "Top ML languages in rank order: Python, R, Java, Julia, Scala, C++, JavaScript, Lisp, Haskell, Go. Why Python: "
        "easy-to-read syntax, extensive libraries and frameworks, strong community support, flexibility, compatibility with "
        "other languages, scalability and performance.",
        [("Libraries trap", "Anaconda is a distribution and Jupyter is an interactive environment, not libraries. SQL is a query language. Formative Q5 key: pandas, SciPy, NumPy.")],
        [("Python Tools", ["Name", "What The Slide Says"],
          [["Scikit-learn", "The most prominent Python library for ML"], ["NumPy", "Fundamental package for scientific computing"],
           ["SciPy", "Collection of functions for scientific computing"], ["Matplotlib", "The primary scientific plotting library"],
           ["Seaborn", "Data visualizations"], ["Pandas", "Data wrangling and analysis"], ["TensorFlow", "Machine learning"],
           ["Keras", "Deep learning"], ["PyTorch", "Machine learning"], ["Scrapy", "Web crawling"], ["SQLModel", "Interacts with SQL databases"],
           ["Anaconda", "Python distribution for large-scale data processing"], ["Jupyter Notebook", "Interactive environment in the browser"]])]),
    sec("Data Preprocessing",
        "Real data has incompleteness (missing values), noise (incorrect records), and inconsistency. Without good data, there "
        "is no good model. Data scientists spend 60 percent of their time on cleaning and organization. Six key steps in order: "
        "data profiling, cleansing, reduction, transformation, enrichment, validation. An outlier is an observation distant from "
        "the others that follows a different logic or generative process; one outlier can throw off a regression estimate.",
        [("Outlier words", "The point is the outlier; the process is outlier detection.")],
        [("Errors In A Messy Table", ["Error", "Meaning"],
          [["Missing value", "A blank cell"], ["Invalid value", "A value outside what is allowed"], ["Invalid duplicate item", "The same Id appears twice"],
           ["Value in another column", "Belongs in a different column"], ["Misspelling", "For example Ytali for Italy"],
           ["Incorrect format", "A date in a different format"], ["Attribute dependency", "Columns that contradict each other"]]),
         ("Two Categories", ["Category", "Techniques"],
          [["Data cleansing", "Missing data, noisy data, duplicates"], ["Feature engineering", "Scaling or normalization, data reduction, discretization, feature encoding"]])]),
    sec("Exploratory Data Analysis and the Titanic Example",
        "EDA understands the data, spots patterns and anomalies, tests a hypothesis, or checks assumptions. Bar plots and "
        "histograms visualize the count of values. Titanic example: 1309 passengers, predict survival from the attributes. "
        "Age had 177 missing values and Embarked had 2: remove the rows, or impute (mean imputation for numeric, "
        "most-frequent imputation for categorical; other imputers are median, iterative, and kNN). Column transformation: "
        "standard scaling for numerical data, ordinal encoding for categorical data. Discrete data is countable (number of "
        "students); continuous data lies on an unbroken scale.",
        [("Discrete vs continuous", "Discrete = Digits you can count. Continuous = Can slide anywhere on the scale.")],
        [("EDA Activities", ["Activity", "What It Does"],
          [["Visualization", "Plots and charts; bar plots and histograms show counts"], ["Summary statistics", "Mean, median, variance, standard deviation"],
           ["Outlier detection", "Identifying unusual data points"], ["Correlation analysis", "Relationships between variables"], ["Hypothesis testing", "Testing initial assumptions"]])]),
    sec("Deployment and Data Ethics",
        "Deployment stages: training, validation, deployment, monitoring (models can drift). Best practices: right "
        "infrastructure, versioning and tracking, robust testing and validation, monitoring and alerting. Data ethics has five "
        "principles. The three new rules of data are trust over transactions, insight over identity, flows over silos. Data "
        "subject rights: to be informed, damages, access, erasure or blocking, file a complaint, object, rectify, data "
        "portability. Regulations shown: GDPR and the National Privacy Commission. Data governance is a set of principles "
        "and processes for data collection, management, and use.",
        [("Five principles", "Own it, Tell them, Protect it, Intend well, check Outcomes: Our Team Protects Individuals' Ownership.")],
        [("Five Principles Of Data Ethics", ["Principle", "Meaning"],
          [["Ownership", "People own their personal information; collect it only with consent"], ["Transparency", "Subjects have a right to know how data is collected, stored, used"],
           ["Privacy", "Protect personally identifiable information (PII)"], ["Intention", "Ask why you need the data; malicious intent is unethical"],
           ["Outcomes", "Good intentions can still cause harm; unintended harm to a group is disparate impact"]])]),
    sec("Supervised Learning Basics",
        "Labeled training data has the input (features) and the correct output (label or goal). The objective is to map the "
        "input to the output, y = f(x); example: weather, temperature, and wind speed predict Enjoy Sports yes or no. Two "
        "phases: training and validation, then prediction. Classification has a categorical target; regression has a "
        "continuous target (the slide says regression predicts consecutive numbers (real numbers); the graded formative key "
        "marked 'consecutive numbers' False, so remember: regression = continuous real numbers).",
        [("Q17 rule", "Regression = continuous real numbers. If a true or false says 'consecutive numbers' alone, follow the formative key (False); 'real numbers' is True.")],
        [("Classification vs Regression", ["", "Classification", "Regression"],
          [["Target", "Categorical", "Continuous"], ["Predicts", "One of the class labels", "Real numbers"],
           ["Subtypes", "Binary (two classes), multiple (three or more)", "Simple linear, multivariate"],
           ["Algorithms (slide)", "Random Forest, Decision Tree, Logistic Regression, SVM", "Simple Linear, Multivariate, Decision Tree, Lasso"]])]),
    sec("Generalization, Overfitting, Underfitting and Complexity",
        "Generalization is accurate prediction on new, unseen data. Overfitting fits the training set too closely (memorized, "
        "good on train, poor on new data). Underfitting is too simple and does badly even on the training set. On the "
        "complexity curve, training accuracy keeps rising, test accuracy peaks at the sweet spot and then falls; left is "
        "underfitting and right is overfitting. Bias = error from wrong or too-simple assumptions; variance = error from "
        "sensitivity to noise. Low bias and low variance is the good model (dartboard picture). More varied data allows a more "
        "complex model; duplicating the same points does not help.",
        [("Under and over", "Under = Underbuilt (bad everywhere). Over = Overthinks (aces training, flops on new data)."),
         ("Complexity trap", "Low complexity is underfitting, not overfitting.")],
        [("Fit Problems", ["Term", "Train", "Test", "Cause"],
          [["Generalization", "Good", "Good", "The goal"], ["Overfitting", "Very good", "Poor", "Too complex, high variance"], ["Underfitting", "Poor", "Poor", "Too simple, high bias"]])]),
    sec("R-Squared",
        "R2 = 1 - sum of (y - y-hat) squared over sum of (y - y-bar) squared. Perfect prediction gives 1, predicting the "
        "average (constant model on y_train) gives 0, and predicting worse than the average gives a negative number. "
        "score() returns R2 for regressors and accuracy for classifiers.",
        [("Report card", "R2 is a report card against guessing the average: 1 perfect, 0 no better than the average, below 0 worse.")],
        [("R2 Values", ["Situation", "R2"],
          [["Perfect prediction", "1"], ["Predicts the average (constant model)", "0"], ["Worse than the average", "Negative"]])]),
    sec("k-Nearest Neighbors",
        "k-NN is the simplest ML algorithm; building the model is only storing the training dataset. Classification votes "
        "(majority class among k neighbors); regression averages the neighbors. Euclidean distance is the default. Small k is "
        "more complex (jagged boundary, bias down, variance up, overfitting); large k is less complex (smooth, bias up, "
        "variance down, underfitting). Training accuracy falls as n_neighbors grows; test accuracy is best somewhere in the middle.",
        [("k and complexity", "Small k = Small crowd = Super complex = Overfit. Big k = Big crowd = Blurry average = Underfit."),
         ("Q9 and Q10", "A small k does NOT make the model less complex. Low complexity is underfitting.")],
        [("Small k vs Large k", ["", "Small k (1 neighbor)", "Large k (9 neighbors)"],
          [["Boundary", "Jagged, unsteady", "Smoother"], ["Complexity", "More complex", "Less complex"], ["Risk", "Overfitting", "Underfitting"]]),
         ("k-NN Strengths And Weaknesses", ["Strengths", "Weaknesses"],
          [["Easy to understand; works without special adjustments; good first model", "Slow with many features or samples; poor on sparse data"]])]),
    sec("Linear Models and Linear Regression (OLS)",
        "Linear models predict with a linear function of the features: y-hat = w[0]*x[0] + ... + w[p]*x[p] + b, where w is the "
        "weight or coefficient and b is the intercept (also offset or bias). Stored in coef_ and intercept_. Linear regression "
        "(OLS) finds w and b that minimize the mean squared error on the training set. Wave dataset: R2 about 0.66 on both "
        "train and test means underfitting. Extended Boston (506 samples, 13 original plus 91 product features): very accurate on "
        "train, much worse on test means overfitting.",
        [("Names for b", "w = Weight = slope. b = Bias = intercept = offset."),
         ("Reading scores", "Close scores, mediocre = underfit. Big gap, high train = overfit.")],
        [("Symbols", ["Symbol", "Meaning"],
          [["x[0] to x[p]", "The features"], ["w[0] to w[p]", "Weights or coefficients (slopes)"], ["b", "Intercept, offset, or bias"], ["y-hat", "The prediction"]])]),
]

MID_EXTRA = [
    sec("Ridge Regression",
        "Same prediction formula as OLS, but the coefficients are also kept as small as possible (close to zero but not zero). "
        "That is regularization, explicitly restricting a model to avoid overfitting; Ridge uses L2. Cost = MSE + alpha * sum of "
        "w squared. Larger alpha means a larger penalty and smaller w. Default alpha is 1.0. On Boston, Ridge train 0.89 is lower "
        "and test 0.75 is higher than OLS. With enough data, regularization matters less.",
        [("Alpha", "Alpha up, All weights shrink toward zero. A bigger alpha is a bigger fine."),
         ("Q13", "A larger alpha does NOT make the penalty lesser. Ridge weights approach zero but never reach it.")],
        [("Ridge vs OLS", ["", "OLS", "Ridge"], [["Train score", "Higher", "Lower"], ["Test score", "Lower", "Higher"], ["Overfitting", "More", "Less (more restricted)"]])]),
    sec("Lasso",
        "Lasso also keeps coefficients near zero, with L1 regularization. Cost = MSE + alpha * sum of absolute w. Some "
        "coefficients become exactly zero, so some features are ignored. Alpha 1.0 underfits (4 of 105 features); lowering "
        "alpha used 33 of 105 features and did slightly better than Ridge; alpha 0.0001 (train 0.95, test 0.64, 96 features) "
        "behaves like linear regression.",
        [("L1 and L2", "L1 = Leaves out features (zeros). L2 = Loves them all a little (shrinks, keeps).")],
        [("Ridge vs Lasso", ["", "Ridge", "Lasso"],
          [["Penalty", "L2", "L1"], ["Weights", "Approach zero, never exactly zero", "Can be exactly zero"],
           ["Prefer when", "Generally preferred", "Few features matter, or you want an easy-to-read model"]])]),
    sec("Logistic Regression and LinearSVC",
        "Linear models for classification: positive class (+1) if the formula is greater than 0, negative (-1) if less than 0. "
        "The boundary is a line, plane, or hyperplane. Logistic regression is a classification algorithm despite its name; it "
        "outputs a probability from 0 to 1 using the sigmoid function and a threshold. Parameter C: higher C means less "
        "regularization, low C pushes w toward zero. Default C = 1 with L2; L1 gives a more interpretable model.",
        [("C vs alpha", "High C = weak regularization; high alpha = strong regularization."),
         ("Remember", "C = Control is loose when high. Alpha = Accuse harder when high.")]),
    sec("Naive Bayes",
        "Similar to linear models, but training is faster. They learn by looking at each feature individually and collecting "
        "simple per-class statistics. Alpha controls complexity (larger alpha, simpler model). Good with sparse, "
        "high-dimensional data and not parameter sensitive.",
        [("Which NB", "Gaussian = Grades on a scale (continuous). Bernoulli = Binary. Multinomial = Many counts.")],
        [("Naive Bayes Types", ["Classifier", "Data"],
          [["GaussianNB", "Continuous data"], ["BernoulliNB", "Binary data, text data"], ["MultinomialNB", "Integer count data, text data"]])]),
    sec("Decision Trees",
        "Decision trees learn a hierarchy of if/else questions (tests); the algorithm picks the most informative test. In the "
        "animal tree: root node (Has feathers?), nodes with true and false edges, and terminal nodes (Hawk, Penguin, Dolphin, "
        "Bear). A prediction returns the majority target of the region. Trees are not affected by feature scale, but they cannot "
        "extrapolate: on the RAM price data the prediction stays flat past the training range. Visualize with export_graphviz.",
        [("Tree parts", "Root at the top, Edges are the true/false arrows, Terminal nodes give the answer.")]),
    sec("Random Forest and Gradient Boosting",
        "Ensembles combine models; both use decision trees. A random forest builds independent trees from bootstrap samples "
        "(drawn with replacement, about one third of points missing) and averages them; key parameters n_estimators and "
        "max_features. Gradient boosting builds shallow trees (depth 5 or less) one after another, each correcting the previous "
        "one's error; key parameters n_estimators, learning_rate (default 0.1), max_depth. Cancer data: forest 97 percent; "
        "boosting at defaults 100 percent on train (overfitting), fixed by limiting depth or lowering the learning rate.",
        [("Forest vs boosting", "Forest = many independent trees VOTE. Boosting = trees take TURNS fixing the last one's mistakes.")],
        [("Random Forest vs Gradient Boosting", ["", "Random Forest", "Gradient Boosting"],
          [["Trees", "Independent, bootstrap samples", "Shallow, built in turn"], ["Idea", "Average to reduce overfitting", "Each tree fixes the previous error"],
           ["Parameters", "n_estimators, max_features", "n_estimators, learning_rate, max_depth"], ["Weakness", "Hard to analyze, slow, poor on large sparse data", "Sensitive to parameters, longer training"]])]),
    sec("Kernelized Support Vector Machines",
        "Kernel SVMs handle nonlinear problems a hyperplane cannot solve (SVC for classification, SVR for regression). Support "
        "vectors define the boundary and the kernel trick gives complex boundaries with few features. gamma sets the Gaussian "
        "kernel width (small gamma = large radius = simpler); C limits each point's influence (small C = very restricted). "
        "SVMs are sensitive to scale: rescale to 0 to 1 with MinMaxScaler. They are slow beyond about 100,000 samples.",
        [("SVM knobs", "Small gamma and small C both make the model simpler. Scale to 0-1 first.")]),
]

CRAM_SA1 = [
    ("Definition", "ML = extracting knowledge from data; learns from data or experience to predict with minimal human intervention. Samuel, 1959. AI contains ML contains Deep Learning."),
    ("E, T, P", "Performance at task T, measured by P, improves with experience E."),
    ("Rule-based vs ML", "Rule-based = condition, manually specified rules. ML = data, rules learned automatically."),
    ("Types and workflow", "Four types in the picture (adds semi-supervised). Workflow: project setup, data preparation, modeling, deployment."),
    ("Python", "Python is number 1 (then R, Java). pandas, NumPy, SciPy, Matplotlib, Seaborn; Anaconda and Jupyter are not libraries."),
    ("Preprocessing", "Incompleteness, noise, inconsistency. Steps: profiling, cleansing, reduction, transformation, enrichment, validation. 60 percent of time is cleaning."),
    ("Outliers and EDA", "Outlier = distant point; outlier detection = the process. Missing values: remove rows or impute (mean, most frequent)."),
    ("Data types", "Discrete = countable. Continuous = unbroken scale. Classification = categorical target; regression = continuous target."),
    ("Fit", "Generalization = good on unseen data. Underfitting = too simple, high bias. Overfitting = memorized, high variance. Low bias + low variance = good."),
    ("k-NN", "Small k = complex = overfit. Large k = simple = underfit. Vote for classes, average for regression, Euclidean default."),
    ("R2", "1 = perfect, 0 = predicts the mean, negative = worse than the mean. score(): regressor R2, classifier accuracy."),
    ("Linear model", "y-hat = w*x + b; b = intercept = offset = bias. OLS minimizes mean squared error on training data."),
]
CRAM_MID = [
    ("Ridge and Lasso", "Ridge = L2, shrinks, never exactly zero, larger alpha = larger penalty. Lasso = L1, some weights exactly zero."),
    ("Logistic Regression", "Classification (sigmoid, threshold). Higher C = less regularization."),
    ("Naive Bayes", "Each feature alone with per-class stats. Gaussian continuous, Multinomial counts, Bernoulli binary."),
    ("Trees", "If/else tests; cannot extrapolate; no scaling needed. Forest = independent bootstrapped trees averaged. Boosting = shallow trees fixing the previous error, learning rate 0.1."),
    ("SVM", "Kernel trick for nonlinear data; scale to 0-1; small gamma and small C = simpler."),
]


def code_section(heading, summary, blocks, aids=(), tables=(), mistakes=()):
    """A notes section whose worked examples are code: each line of code is one step."""
    s = sec(heading, summary, aids, tables)
    s["worked_examples"] = [
        {"problem": title, "steps": [ln for ln in code.strip("\n").split("\n") if ln.strip()], "answer": shows}
        for title, code, shows in blocks
    ]
    s["common_mistakes"] = list(mistakes)
    return s


CODE_SECTIONS = [
    code_section(
        "Code and Imports: Notebook Code",
        "Reported exam format: fill-in-the-blank imports (like import ____ as np) and two 7-point code items where you "
        "complete missing code from the module. The table lists every import the module uses. The examples below are the "
        "prof's M2 notebook and the Module 1 preprocessing notebook, one line of code per step.",
        NOTEBOOK,
        [("Import names", "Package = what it does: datasets, model_selection (splitting), neighbors, impute, preprocessing "
                          "(scalers), metrics. The class name is the one with capitals."),
         ("Pipeline order", "Load, split, instantiate, fit on train, predict, score on test.")],
        [("Imports From The Module", ["What", "Import line"], IMPORT_ROWS)],
        ["train_test_split returns four things in the order X_train, X_test, y_train, y_test.",
         "fit takes train data; score takes test data. n_neighbors is the k parameter.",
         "Double brackets df[['Age']] give a table (2-D); single brackets give one column. fit_transform needs the table.",
         "Naive Bayes has no code on the slides: only the class names GaussianNB (continuous), BernoulliNB (binary), MultinomialNB (counts)."]),
    code_section(
        "Code: M2 Slide Code",
        "Everything here is code printed in the M2 slide images, read slide by slide. Variable names are the slides' own: "
        "clf (k-NN), reg (regressor), ridge, lasso, logreg, tree, forest, gbrt, svc.",
        SLIDES,
        [("Same pattern everywhere", "Create the model, fit(X_train, y_train), then score on train and on test. "
                                      "Classifiers report accuracy; regressors report R squared.")],
        [],
        ["The slides scale the SVM data by hand (min_on_training, range_on_training), not with MinMaxScaler. The M1 notebook uses MinMaxScaler.",
         "The test set must reuse the training set's min and range, never its own.",
         "Lasso with a small alpha needs a bigger max_iter.",
         "Trees and forests need no scaling; SVM and k-NN do."]),
]

SELF_CHECK = [
    {"question": "Fill in the blank: " + q, "answer": line}
    for q, _, line in IMPORTS + CODE[:12]
]
CRAM_CODE = [
    ("Code", "load, train_test_split (X_train, X_test, y_train, y_test), KNeighborsClassifier(n_neighbors=k), fit(train), "
             "predict(test), score(test). SimpleImputer(strategy='mean') and StandardScaler/MinMaxScaler use fit_transform(df[['col']])."),
]


def note(title, sections, cram, self_check=()):
    return {
        "title": title,
        "subject": "Machine Learning Algorithm",
        "module_ids": [],
        "content": {
            "sections": sections,
            "formula_sheet": [],
            "self_check": list(self_check),
            "cram_sheet": [{"topic": t, "remember": r} for t, r in cram],
        },
    }


notes = [
    note("ML SA1 Reviewer Notes", SA1_SECTIONS, CRAM_SA1),
    note("ML Midterm Reviewer Notes", SA1_SECTIONS + MID_EXTRA + CODE_SECTIONS, CRAM_SA1 + CRAM_MID + CRAM_CODE, SELF_CHECK),
]
with open(os.path.join(HERE, "andyhub_ml_notes.json"), "w", encoding="utf-8") as fh:
    json.dump(notes, fh, indent=1)
for x in notes:
    c = x["content"]
    print(x["title"], len(c["sections"]), "sections", sum(len(s["memory_aids"]) for s in c["sections"]), "aids",
          sum(len(s["comparisons"]) for s in c["sections"]), "tables", len(c["cram_sheet"]), "cram")
