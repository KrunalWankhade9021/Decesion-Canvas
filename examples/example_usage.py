from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from decisioncanvas import plot_decision_boundary

data = load_iris()
X, y = data.data, data.target
class_names = data.target_names

model = LogisticRegression(max_iter=500)
plot_decision_boundary(
    model=model,
    X=X,
    y=y,
    class_names=list(class_names),
    standardize=True,
    pca_components=2,
    grid_resolution=250,
    alpha=0.4,
    title="Logistic Regression Decision Boundary on Iris (PCA-2D)",
    fit_model=True
)
