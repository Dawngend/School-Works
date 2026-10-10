"""100 practice items for the CS0075 midterm: 40 flashcards (multiple choice), 50 fill-in-the-blank (25 imports,
25 code), 10 enumerations. Facts come from the midterm reviewer and the M2 picture slides read through andy read.
Usage: python ml_100_items.py pdf     (builds the PDF + docx)
       python ml_100_items.py db      (adds the deck to the local AndyHub database)"""
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = r"D:\School-Works\Machine Learning Algorithm"
HUB = r"D:\Personal Projects\All In One Reviewer"
DECK_NAME = "ML Midterm 100 Practice Items"

# (question, correct, [three wrong])
FLASH = [
    ("In the four-stage ML workflow, which stage includes splitting the data?", "Data preparation", ["Project setup", "Modeling", "Deployment"]),
    ("In the four-stage ML workflow, which stage includes hyperparameter tuning?", "Modeling", ["Data preparation", "Project setup", "Deployment"]),
    ("Which language ranks number 1 for machine learning in the slides?", "Python", ["R", "Java", "Julia"]),
    ("Which Python library from the slides is used for web crawling?", "Scrapy", ["Seaborn", "SQLModel", "Keras"]),
    ("Which Python tool from the slides is a distribution for large-scale data processing and scientific computing?", "Anaconda", ["Pandas", "Jupyter Notebook", "SciPy"]),
    ("What drives a traditional rule-based algorithm?", "A condition (true goes to one code, false to another)", ["Training data", "A learned model", "An accuracy score"]),
    ("What is the key difference when machine learning is compared with rule-based programming?", "The rules are learned automatically from data", ["The rules are written by hand", "It needs no data", "It only works for simple rules"]),
    ("According to the pie chart, what do data scientists spend most of their time on?", "Data cleaning and organization (60 percent)", ["Data mining", "Improving algorithms", "Creating training sets"]),
    ("Which three problems does the slide say real-world data has?", "Incompleteness, noise, inconsistency", ["Size, speed, cost", "Bias, variance, noise", "Missing, scaled, encoded"]),
    ("In the messy table, the same Id appearing twice is marked as what?", "An invalid duplicate item", ["A missing value", "A misspelling", "An attribute dependency"]),
    ("\"Identifies unusual data points\" describes which EDA activity?", "Outlier detection", ["Correlation analysis", "Hypothesis testing", "Summary statistics"]),
    ("Which is an example of discrete data?", "Number of students in a class", ["Height", "Weight", "Temperature"]),
    ("On the Titanic data, which imputation fits the numeric Age column?", "Mean imputation", ["Most-frequent imputation", "Dropping the column", "Ordinal encoding"]),
    ("On the Titanic data, which imputation fits the categorical Embarked column?", "Most-frequent imputation", ["Mean imputation", "Standard scaling", "Median imputation"]),
    ("On the Titanic data, which transformation is applied to Age and Fare?", "Standard scaling", ["Ordinal encoding", "Most-frequent imputation", "Feature selection"]),
    ("Unintended harm to a group, even from good intentions, is called what?", "Disparate impact", ["Data drift", "Informed consent", "Data portability"]),
    ("What does a regression algorithm predict?", "Continuous real numbers", ["Class labels", "Clusters", "Rules"]),
    ("A model that memorizes the training data and does poorly on new data is...", "Overfitting (high variance)", ["Underfitting (high bias)", "Generalizing well", "Regularized"]),
    ("What does a very small k do to a k-NN model?", "Makes it more complex and prone to overfitting", ["Makes it simpler and underfit", "Has no effect", "Makes it linear"]),
    ("What does a very large k do to a k-NN model?", "Makes it simpler and prone to underfitting", ["Makes it more complex and overfit", "Has no effect", "Removes the need for training data"]),
    ("What does score() return for a classifier, and for a regressor?", "Accuracy for a classifier, R squared for a regressor", ["R squared for both", "Accuracy for both", "Mean squared error for both"]),
    ("An R squared below zero means the model is...", "Worse than always predicting the mean", ["Perfect", "Exactly as good as the mean", "Overfit by a small amount"]),
    ("In y-hat = w*x + b, what is b also called?", "The intercept (offset or bias)", ["The slope", "The weight vector", "The learning rate"]),
    ("What does ordinary least squares (OLS) minimize?", "Mean squared error on the training set", ["Absolute error on the test set", "The number of features", "The size of the weights"]),
    ("In Ridge regression, what does a larger alpha do?", "Applies a bigger penalty and a simpler model", ["Applies a smaller penalty", "Removes the penalty", "Adds more features"]),
    ("Which model can set weights to exactly zero?", "Lasso (L1)", ["Ridge (L2)", "Plain LinearRegression", "k-NN"]),
    ("Ridge regression uses which kind of penalty?", "L2 regularization", ["L1 regularization", "No penalty", "A tree-depth penalty"]),
    ("In LogisticRegression, what does a high C mean?", "Weaker regularization", ["Stronger regularization", "More neighbors", "A smaller tree"]),
    ("Despite its name, logistic regression is used for what?", "Classification", ["Regression", "Clustering", "Dimension reduction"]),
    ("Which Naive Bayes class is for continuous features?", "GaussianNB", ["BernoulliNB", "MultinomialNB", "CategoricalNB"]),
    ("Which Naive Bayes class is for integer count data such as word counts?", "MultinomialNB", ["GaussianNB", "BernoulliNB", "LinearSVC"]),
    ("Which of these models needs its features scaled?", "SVM", ["Decision tree", "Random forest", "Gradient boosting"]),
    ("What is a random forest?", "An average of many independent trees built on bootstrap samples", ["One very deep tree", "Trees built in turn, each fixing the last", "A linear model with many features"]),
    ("How does gradient boosting build its trees?", "One after another, each correcting the previous trees' errors", ["All at once, independently", "From a single bootstrap sample", "Without any depth limit"]),
    ("What is the default learning rate of GradientBoostingClassifier?", "0.1", ["1.0", "0.01", "0.5"]),
    ("What is a limitation of a decision tree regressor?", "It cannot extrapolate beyond the training data range", ["It needs scaled features", "It only handles two features", "It cannot overfit"]),
    ("In an RBF-kernel SVM, what does a small gamma do?", "Gives a wide radius and a simpler model", ["Gives a narrow radius and a more complex model", "Turns off the kernel", "Doubles the number of support vectors"]),
    ("In an SVM, what does a small C do?", "Restricts the model heavily", ["Lets every point influence it freely", "Switches to a linear kernel", "Scales the features"]),
    ("Which is a weakness of SVMs?", "Slow with many samples and sensitive to feature scaling", ["They cannot do classification", "They only fit linear data", "They need no parameter tuning"]),
    ("On the breast cancer data, the default SVC on unscaled features scores train 1.00 and test 0.63. What does that show?", "Severe overfitting caused by unscaled features", ["Underfitting", "A perfect model", "Too few samples"]),
]

# (question, answer, full line shown after reveal)
IMPORTS = [
    ("import ____ as np", "numpy", "import numpy as np"),
    ("import pandas as ____", "pd", "import pandas as pd"),
    ("import matplotlib.____ as plt", "pyplot", "import matplotlib.pyplot as plt"),
    ("import ____   (the textbook's plotting and dataset helper package)", "mglearn", "import mglearn"),
    ("from sklearn.____ import load_iris", "datasets", "from sklearn.datasets import load_iris"),
    ("from sklearn.datasets import ____   (the 569-sample cancer data)", "load_breast_cancer", "from sklearn.datasets import load_breast_cancer"),
    ("from sklearn.datasets import ____   (the two_moons data)", "make_moons", "from sklearn.datasets import make_moons"),
    ("from sklearn.model_selection import ____", "train_test_split", "from sklearn.model_selection import train_test_split"),
    ("from sklearn.____ import KNeighborsClassifier", "neighbors", "from sklearn.neighbors import KNeighborsClassifier"),
    ("from sklearn.neighbors import ____   (k-NN for a continuous target)", "KNeighborsRegressor", "from sklearn.neighbors import KNeighborsRegressor"),
    ("from sklearn.impute import ____", "SimpleImputer", "from sklearn.impute import SimpleImputer"),
    ("from sklearn.preprocessing import ____   (z-score scaling)", "StandardScaler", "from sklearn.preprocessing import StandardScaler"),
    ("from sklearn.preprocessing import ____   (scales to 0 to 1)", "MinMaxScaler", "from sklearn.preprocessing import MinMaxScaler"),
    ("from sklearn.____ import accuracy_score", "metrics", "from sklearn.metrics import accuracy_score"),
    ("from sklearn.linear_model import ____   (ordinary least squares)", "LinearRegression", "from sklearn.linear_model import LinearRegression"),
    ("from sklearn.linear_model import ____   (L2 penalty)", "Ridge", "from sklearn.linear_model import Ridge"),
    ("from sklearn.linear_model import ____   (L1 penalty, can zero out weights)", "Lasso", "from sklearn.linear_model import Lasso"),
    ("from sklearn.linear_model import ____   (a classifier despite its name)", "LogisticRegression", "from sklearn.linear_model import LogisticRegression"),
    ("from sklearn.____ import SVC", "svm", "from sklearn.svm import SVC"),
    ("from sklearn.svm import ____   (the linear SVM)", "LinearSVC", "from sklearn.svm import LinearSVC"),
    ("from sklearn.____ import DecisionTreeClassifier", "tree", "from sklearn.tree import DecisionTreeClassifier"),
    ("from sklearn.tree import ____   (writes a .dot file)", "export_graphviz", "from sklearn.tree import export_graphviz"),
    ("import ____   (shows the .dot file inside Python)", "graphviz", "import graphviz"),
    ("from sklearn.ensemble import ____   (many independent trees)", "RandomForestClassifier", "from sklearn.ensemble import RandomForestClassifier"),
    ("from sklearn.____ import GradientBoostingClassifier", "ensemble", "from sklearn.ensemble import GradientBoostingClassifier"),
]

CODE = [
    ("X_train, X_test, y_train, y_test = train_test_split(X, y, ____=0)", "random_state", "train_test_split(X, y, random_state=0)"),
    ("train_test_split(cancer.data, cancer.target, ____=cancer.target, random_state=66)   (keeps class proportions)", "stratify", "train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=66)"),
    ("knn = KNeighborsClassifier(____=3)", "n_neighbors", "knn = KNeighborsClassifier(n_neighbors=3)"),
    ("knn.____(X_train, y_train)   (trains the model)", "fit", "knn.fit(X_train, y_train)"),
    ("prediction = knn.____(X_test)", "predict", "prediction = knn.predict(X_test)"),
    ("print(\"Test set score: {:.2f}\".format(knn.____(X_test, y_test)))", "score", "knn.score(X_test, y_test)"),
    ("X_new = np.____([[40, 80, 70, 30]])", "array", "X_new = np.array([[40, 80, 70, 30]])   (2-D, so a list inside a list)"),
    ("reg = ____(n_neighbors=3)   (k-NN for a continuous target)", "KNeighborsRegressor", "reg = KNeighborsRegressor(n_neighbors=3)"),
    ("lr = LinearRegression().____(X_train, y_train)", "fit", "lr = LinearRegression().fit(X_train, y_train)"),
    ("lr.coef_ holds the weights. Which attribute holds the intercept? lr.____", "intercept_", "lr.intercept_"),
    ("lasso001 = Lasso(____=0.01, max_iter=100000).fit(X_train, y_train)", "alpha", "Lasso(alpha=0.01, max_iter=100000)"),
    ("lasso001 = Lasso(alpha=0.01, ____=100000).fit(X_train, y_train)", "max_iter", "Lasso(alpha=0.01, max_iter=100000)"),
    ("logreg100 = LogisticRegression(____=100).fit(X_train, y_train)", "C", "LogisticRegression(C=100)"),
    ("lr_l1 = LogisticRegression(C=C, penalty=\"____\", solver='liblinear')   (the L1 penalty)", "l1", "LogisticRegression(C=C, penalty=\"l1\", solver='liblinear')"),
    ("lr_l1 = LogisticRegression(C=C, penalty=\"l1\", solver='____')", "liblinear", "LogisticRegression(C=C, penalty=\"l1\", solver='liblinear')"),
    ("tree = DecisionTreeClassifier(____=4, random_state=0)   (pre-pruning)", "max_depth", "DecisionTreeClassifier(max_depth=4, random_state=0)"),
    ("forest = RandomForestClassifier(____=100, random_state=0)", "n_estimators", "RandomForestClassifier(n_estimators=100, random_state=0)"),
    ("gbrt = GradientBoostingClassifier(random_state=0, ____=0.01)", "learning_rate", "GradientBoostingClassifier(random_state=0, learning_rate=0.01)"),
    ("svm = SVC(kernel='____', C=10, gamma=0.1).fit(X, y)", "rbf", "SVC(kernel='rbf', C=10, gamma=0.1)"),
    ("svc = SVC(____=1000)   (the improvement on scaled data)", "C", "svc = SVC(C=1000)"),
    ("min_on_training = X_train.min(____=0)", "axis", "min_on_training = X_train.min(axis=0)"),
    ("range_on_training = (X_train - min_on_training).____(axis=0)", "max", "range_on_training = (X_train - min_on_training).max(axis=0)"),
    ("X_test_scaled = (X_test - ____) / range_on_training   (reuse the TRAINING values)", "min_on_training", "X_test_scaled = (X_test - min_on_training) / range_on_training"),
    ("imputer = SimpleImputer(strategy='____', missing_values=np.nan)   (fill with the average)", "mean", "SimpleImputer(strategy='mean', missing_values=np.nan)"),
    ("df['Age'] = imputer.____(df[['Age']]).ravel()", "fit_transform", "df['Age'] = imputer.fit_transform(df[['Age']]).ravel()"),
]

# (question, [items], note)
ENUM = [
    ("Name the four stages of the ML workflow.", ["Project setup", "Data preparation", "Modeling", "Deployment"]),
    ("Name the four types of machine learning shown in the picture.", ["Supervised", "Unsupervised", "Semi-supervised", "Reinforcement"]),
    ("Name the three data quality problems.", ["Incompleteness", "Noise", "Inconsistency"]),
    ("Name the five data ethics principles.", ["Ownership", "Transparency", "Privacy", "Intention", "Outcomes"]),
    ("Name the six key steps of data preprocessing.", ["Profiling", "Cleansing", "Reduction", "Transformation", "Enrichment", "Validation"]),
    ("What do E, T and P stand for in the formal definition of ML?", ["Experience", "Task", "Performance"]),
    ("Name the three Naive Bayes classes in scikit-learn.", ["GaussianNB", "BernoulliNB", "MultinomialNB"]),
    ("train_test_split returns four items. Name them.", ["X_train", "X_test", "y_train", "y_test"]),
    ("Name the three linear regression models covered in the slides.", ["Linear Regression", "Ridge", "Lasso"]),
    ("Name the two main parameters of an RBF-kernel SVM.", ["C", "gamma"]),
]


def all_items():
    rnd = random.Random(7)
    items = []
    for q, correct, wrong in FLASH:
        opts = [correct] + list(wrong)
        rnd.shuffle(opts)
        items.append({"type": "multiple_choice", "q": q, "answer": correct, "options": opts, "label": "Flashcard"})
    for q, ans, line in IMPORTS:
        items.append({"type": "problem", "q": "Fill in the blank: " + q, "answer": ans, "steps": ["Full line: " + line], "label": "Import"})
    for q, ans, line in CODE:
        items.append({"type": "problem", "q": "Fill in the blank: " + q, "answer": ans, "steps": ["Full code: " + line], "label": "Code"})
    for q, expected in ENUM:
        items.append({"type": "enumeration", "q": q, "answer": ", ".join(expected), "expected": expected, "label": "List"})
    return items


def build_pdf(items):
    sys.path.insert(0, HERE)
    from notes_lib import Notes
    n = Notes("ML Midterm: 100 Practice Items",
              "CS0075 Machine Learning Algorithm. 40 flashcards, 25 import blanks, 25 code blanks, 10 lists. "
              "Facts and code come from the midterm reviewer and the M2 slides. The answer key is at the end.")
    n.h1("Part A. Flashcards (1 to 40)")
    count = 0
    for it in items:
        if it["type"] == "multiple_choice":
            count += 1
            n.p(f"**{count}.** {it['q']}")
            for letter, opt in zip("ABCD", it["options"]):
                n.p(f"      {letter}.  {opt}")
    n.h1("Part B. Fill In The Blank: Imports (41 to 65)")
    for it in items:
        if it["type"] == "problem" and it["label"] == "Import":
            count += 1
            n.p(f"**{count}.** {it['q'][len('Fill in the blank: '):]}")
    n.h1("Part C. Fill In The Blank: Code (66 to 90)")
    for it in items:
        if it["type"] == "problem" and it["label"] == "Code":
            count += 1
            n.p(f"**{count}.** {it['q'][len('Fill in the blank: '):]}")
    n.h1("Part D. Lists (91 to 100)")
    for it in items:
        if it["type"] == "enumeration":
            count += 1
            n.p(f"**{count}.** {it['q']} ({len(it['expected'])} items)")
    n.pagebreak()
    n.h1("Answer Key")
    rows = []
    for i, it in enumerate(items, 1):
        extra = it["steps"][0] if it["type"] == "problem" else ""
        rows.append([str(i), it["answer"], extra])
    n.table(["No.", "Answer", "Full line (blanks only)"], rows, [0.5, 2.5, 3.5])
    return n.save(os.path.join(OUT, "PAMESA - ML Midterm 100 Practice Items.docx"))


def add_to_db(items):
    sys.path.insert(0, HUB)
    os.chdir(HUB)
    import database
    from repositories import NewCard
    database.init_db()
    cards = []
    for it in items:
        if it["type"] == "multiple_choice":
            cards.append(NewCard("multiple_choice", it["q"], it["answer"], it["options"]))
        elif it["type"] == "problem":
            payload = {"final_answer": it["answer"], "solution_steps": it["steps"]}
            cards.append(NewCard("problem", it["q"], it["answer"], payload))
        else:
            cards.append(NewCard("enumeration", it["q"], json.dumps(it["expected"]), it["expected"]))
    deck_id = database.create_deck_with_cards(DECK_NAME, "M1-MAIN-1.pdf, M2 - Supervised Learning - Main.pdf",
                                              "Machine Learning Algorithm", cards)
    print("new deck id", deck_id, "cards", len(cards))


if __name__ == "__main__":
    items = all_items()
    assert len(items) == 100, len(items)
    mode = sys.argv[1] if len(sys.argv) > 1 else "pdf"
    if mode == "pdf":
        print(build_pdf(items))
    elif mode == "db":
        add_to_db(items)
