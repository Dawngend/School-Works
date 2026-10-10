"""Code blocks for the AndyHub midterm notes. Source: prof's M2.ipynb, the M1 preprocessing notebook, and the M2
picture slides (read with andy read). Each block = (title, code, what it shows)."""

IMPORT_ROWS = [
    ["NumPy", "import numpy as np"],
    ["pandas", "import pandas as pd"],
    ["Matplotlib", "import matplotlib.pyplot as plt"],
    ["mglearn", "import mglearn"],
    ["Legend patches", "import matplotlib.patches as mpatches"],
    ["Iris data", "from sklearn.datasets import load_iris"],
    ["Breast cancer data", "from sklearn.datasets import load_breast_cancer"],
    ["Moons data", "from sklearn.datasets import make_moons"],
    ["California housing", "from sklearn.datasets import fetch_california_housing"],
    ["Forge / wave data", "mglearn.datasets.make_forge() and mglearn.datasets.make_wave(n_samples=40)"],
    ["Train/test split", "from sklearn.model_selection import train_test_split"],
    ["k-NN classifier", "from sklearn.neighbors import KNeighborsClassifier"],
    ["k-NN regressor", "from sklearn.neighbors import KNeighborsRegressor"],
    ["Accuracy", "from sklearn.metrics import accuracy_score"],
    ["Missing-value imputer", "from sklearn.impute import SimpleImputer"],
    ["Z-score scaling", "from sklearn.preprocessing import StandardScaler"],
    ["0 to 1 scaling", "from sklearn.preprocessing import MinMaxScaler"],
    ["Linear regression", "from sklearn.linear_model import LinearRegression"],
    ["Ridge", "from sklearn.linear_model import Ridge"],
    ["Lasso", "from sklearn.linear_model import Lasso"],
    ["Logistic regression", "from sklearn.linear_model import LogisticRegression"],
    ["Linear SVM", "from sklearn.svm import LinearSVC"],
    ["Kernel SVM", "from sklearn.svm import SVC"],
    ["Decision tree", "from sklearn.tree import DecisionTreeClassifier (regression: DecisionTreeRegressor)"],
    ["Export a tree", "from sklearn.tree import export_graphviz, then import graphviz"],
    ["Random forest", "from sklearn.ensemble import RandomForestClassifier"],
    ["Gradient boosting", "from sklearn.ensemble import GradientBoostingClassifier"],
]

NOTEBOOK = [
    ("Code 1. k-NN on iris (notebook)", """
from sklearn.datasets import load_iris
iris_dataset = load_iris()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))
X_new = np.array([[40, 80, 70, 30]])
prediction = knn.predict(X_new)
print("Predicted target name:", iris_dataset['target_names'][prediction])
""", "Order: load, split, instantiate with n_neighbors, fit(train), predict, score(test). X_new is 2-D (list inside a list)."),
    ("Code 2. k-NN on breast cancer with the complexity curve (notebook)", """
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
df['target'] = cancer.target
X = df.drop(columns='target')
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=66)
training_accuracy = []
test_accuracy = []
neighbors_settings = range(1, 10)
for n_neighbors in neighbors_settings:
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)
    training_accuracy.append(knn.score(X_train, y_train))
    test_accuracy.append(knn.score(X_test, y_test))
plt.plot(neighbors_settings, training_accuracy, label="training accuracy")
plt.plot(neighbors_settings, test_accuracy, label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, y_train)
""", "stratify=y keeps class proportions the same. 569 samples: 212 malignant, 357 benign. The notebook ends with k = 6 picked from the curve."),
    ("Code 3. Module 1 preprocessing: imputation and scaling", """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
df = pd.read_csv('diabetes_NaN_age 3.csv')
imputer_mean = SimpleImputer(strategy='mean', missing_values=np.nan)
df['Age'] = imputer_mean.fit_transform(df[['Age']]).ravel()
age_mean = df['Age'].mean()
df.loc[df['Age'].isna(), 'Age'] = age_mean
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
""", "fit_transform needs a 2-D input, so df[['Age']] with double brackets; .ravel() flattens it back. StandardScaler = mean 0, std 1. MinMaxScaler = 0 to 1."),
]

SLIDES = [
    ("Code 4. k-NN classifier, slide version (clf)", """
from sklearn.model_selection import train_test_split
X, y = mglearn.datasets.make_forge()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)
print("Test set predictions: {}".format(clf.predict(X_test)))
print("Test set accuracy: {:.2f}".format(clf.score(X_test, y_test)))
""", "The slides call the model clf; the notebook calls it knn. Know both names."),
    ("Code 4b. k-NN complexity curve, slide version", """
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify=cancer.target, random_state=66)
training_accuracy = []
test_accuracy = []
neighbors_settings = range(1, 11)
for n_neighbors in neighbors_settings:
    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    clf.fit(X_train, y_train)
    training_accuracy.append(clf.score(X_train, y_train))
    test_accuracy.append(clf.score(X_test, y_test))
plt.plot(neighbors_settings, training_accuracy, label="training accuracy")
plt.plot(neighbors_settings, test_accuracy, label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
""", "The slide loops k from 1 to 10 (range(1, 11)); the notebook loops 1 to 9."),
    ("Code 5. k-NN regressor", """
from sklearn.neighbors import KNeighborsRegressor
X, y = mglearn.datasets.make_wave(n_samples=40)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
reg = KNeighborsRegressor(n_neighbors=3)
reg.fit(X_train, y_train)
print("Test set predictions:\\n{}".format(reg.predict(X_test)))
print("Test set R^2: {:.2f}".format(reg.score(X_test, y_test)))
""", "For a regressor, score() is R squared, not accuracy."),
    ("Code 6. Linear regression (OLS)", """
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import mglearn
X, y = mglearn.datasets.make_wave(n_samples=60)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
lr = LinearRegression().fit(X_train, y_train)
print("lr.coef_: {}".format(lr.coef_))
print("lr.intercept_: {}".format(lr.intercept_))
print("Training set score: {:.2f}".format(lr.score(X_train, y_train)))
print("Test set score: {:.2f}".format(lr.score(X_test, y_test)))
""", "coef_ holds the weights; intercept_ holds b."),
    ("Code 6b. Ridge and Lasso", """
from sklearn.linear_model import Ridge
ridge = Ridge().fit(X_train, y_train)
print("Training set score: {:.2f}".format(ridge.score(X_train, y_train)))
print("Test set score: {:.2f}".format(ridge.score(X_test, y_test)))
from sklearn.linear_model import Lasso
import numpy as np
lasso = Lasso().fit(X_train, y_train)
lasso001 = Lasso(alpha=0.01, max_iter=100000).fit(X_train, y_train)
lasso00001 = Lasso(alpha=0.0001, max_iter=100000).fit(X_train, y_train)
plt.plot(ridge.coef_, 's', label="Ridge alpha=1")
plt.plot(lasso.coef_, 's', label="Lasso alpha=1")
""", "Ridge default alpha = 1.0. Lasso default alpha = 1.0 underfits (4 of 105 features); alpha=0.01 with max_iter=100000 works; alpha=0.0001 overfits (96 of 105 features)."),
    ("Code 7. Logistic regression and LinearSVC", """
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
import mglearn
for model, ax in zip([LinearSVC(), LogisticRegression()], axes):
    clf = model.fit(X, y)
    mglearn.plots.plot_2d_separator(clf, X, fill=False, eps=0.5, ax=ax, alpha=.7)
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify=cancer.target, random_state=42)
logreg = LogisticRegression().fit(X_train, y_train)
logreg100 = LogisticRegression(C=100).fit(X_train, y_train)
logreg001 = LogisticRegression(C=0.01).fit(X_train, y_train)
lr_l1 = LogisticRegression(C=C, penalty="l1", solver='liblinear').fit(X_train, y_train)
""", "Default C = 1.0 with an L2 penalty (train 0.948, test 0.944). C=100 = weaker regularization; C=0.01 = stronger. penalty='l1' needs solver='liblinear'."),
    ("Code 8. Decision tree and export", """
from sklearn.tree import DecisionTreeClassifier
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify=cancer.target, random_state=42)
tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train, y_train)
print("Accuracy on training set: {:.3f}".format(tree.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(tree.score(X_test, y_test)))
tree = DecisionTreeClassifier(max_depth=4, random_state=0)
tree.fit(X_train, y_train)
from sklearn.tree import export_graphviz
export_graphviz(tree, out_file="tree.dot", class_names=["malignant", "benign"],
                feature_names=cancer.feature_names, impurity=False, filled=True)
import graphviz
with open("tree.dot") as f:
    dot_graph = f.read()
graphviz.Source(dot_graph)
""", "Full tree: train 1.000, test 0.937. max_depth=4 (pre-pruning): train 0.988, test 0.951."),
    ("Code 8b. Tree regressor vs linear regression", """
from sklearn.tree import DecisionTreeRegressor
data_train = ram_prices[ram_prices.date < 2000]
data_test = ram_prices[ram_prices.date >= 2000]
X_train = data_train.date[:, np.newaxis]
y_train = np.log(data_train.price)
tree = DecisionTreeRegressor().fit(X_train, y_train)
linear_reg = LinearRegression().fit(X_train, y_train)
X_all = ram_prices.date[:, np.newaxis]
pred_tree = tree.predict(X_all)
pred_lr = linear_reg.predict(X_all)
price_tree = np.exp(pred_tree)
price_lr = np.exp(pred_lr)
""", "Log-transform the target (np.log), then undo it (np.exp). The tree cannot extrapolate past the training dates."),
    ("Code 9. Random forest", """
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_moons
X, y = make_moons(n_samples=100, noise=0.25, random_state=3)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,
                                                    random_state=42)
forest = RandomForestClassifier(n_estimators=5, random_state=2)
forest.fit(X_train, y_train)
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, random_state=0)
forest = RandomForestClassifier(n_estimators=100, random_state=0)
forest.fit(X_train, y_train)
print("Accuracy on training set: {:.3f}".format(forest.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(forest.score(X_test, y_test)))
""", "n_estimators = number of trees (5 on moons, 100 on breast cancer). The 100-tree forest scores 0.972 on test."),
    ("Code 10. Gradient boosting", """
from sklearn.ensemble import GradientBoostingClassifier
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, random_state=0)
gbrt = GradientBoostingClassifier(random_state=0)
gbrt.fit(X_train, y_train)
print("Accuracy on training set: {:.3f}".format(gbrt.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(gbrt.score(X_test, y_test)))
gbrt = GradientBoostingClassifier(random_state=0, max_depth=1)
gbrt = GradientBoostingClassifier(random_state=0, learning_rate=0.01)
""", "Defaults: n_estimators=100, max_depth=3, learning_rate=0.1. Overfit fixes: lower max_depth or lower learning_rate."),
    ("Code 11. Support vector machines and manual 0-1 scaling", """
from sklearn.svm import LinearSVC
linear_svm = LinearSVC().fit(X, y)
from sklearn.svm import SVC
svm = SVC(kernel='rbf', C=10, gamma=0.1).fit(X, y)
svc = SVC()
svc.fit(X_train, y_train)
min_on_training = X_train.min(axis=0)
range_on_training = (X_train - min_on_training).max(axis=0)
X_train_scaled = (X_train - min_on_training) / range_on_training
X_test_scaled = (X_test - min_on_training) / range_on_training
svc = SVC()
svc.fit(X_train_scaled, y_train)
svc = SVC(C=1000)
svc.fit(X_train_scaled, y_train)
""", "The slides scale by hand, not with MinMaxScaler. The test set reuses the TRAINING min and range. Unscaled SVC: train 1.00, test 0.63. Scaled: 0.948 / 0.951. Scaled with C=1000: 0.988 / 0.972."),
]
