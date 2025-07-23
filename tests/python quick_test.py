from decisioncanvas import plot_decision_boundary
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
plot_decision_boundary(LogisticRegression(max_iter=200), X, y)
