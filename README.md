# 🧠 decisioncanvas

**Effortless, high-quality visualization of classifier decision boundaries.**  
An open-source Python library designed for quick, reliable, and interpretable visualizations of how classification models separate data.

---

## 📌 Overview

`decisioncanvas` helps you create **clear, publication-ready plots** for **any scikit-learn-compatible classifier**. Whether you're working with **2D or high-dimensional data**, the library automatically:

- Applies PCA to reduce dimensions
- Standardizes features
- Visualizes decision boundaries clearly and beautifully

---

## ✨ Features

- ✅ **Simple API**: Just one function call: `plot_decision_boundary(...)`
- 📊 **High-Dimensional Support**: Automatic PCA with explained variance
- 🤖 **Scikit-learn Compatibility**: Works with `LogisticRegression`, `SVC`, `RandomForestClassifier`, `KNeighborsClassifier`, etc.
- 🏷️ **Binary & Multiclass Support**: Handles all class types with auto legends and colors
- ⚖️ **Built-in Standardization**: Ensures fair comparisons
- 🎨 **Customizable**: Grid resolution, alpha, color maps, titles, etc.
- 👨‍🏫 **Beginner-Friendly**: Great for learning, tutorials, and teaching
- 💼 **Production-Ready**: Strong validation and error handling
- 💻 **Open Source (MIT Licensed)**: Free for academic, personal, and commercial use

---

## 🛠️ Installation

```bash
pip install decisioncanvas
````

---

## 🚀 Quick Start

```python
from decisioncanvas import plot_decision_boundary
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
plot_decision_boundary(LogisticRegression(max_iter=300), X, y)
```

---

## 📚 Step-by-Step Workflow Example

### 1️⃣ Import Libraries

```python
from decisioncanvas import plot_decision_boundary
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
```

### 2️⃣ Load and Split Data

```python
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=42, stratify=data.target
)
```

### 3️⃣ Train a Model

```python
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
```

### 4️⃣ Plot Decision Boundary

```python
plot_decision_boundary(
    model,
    X_train,
    y_train,
    class_names=list(data.target_names),
    title='Iris Logistic Regression Decision Boundary'
)
```

---

## ⚙️ Advanced Usage

### 🧠 Use Any Classifier

Supports all `sklearn` classifiers like `SVC`, `RandomForestClassifier`, `KNeighborsClassifier`, etc.

### 🎨 Customize Appearance

```python
plot_decision_boundary(
    model,
    X,
    y,
    grid_resolution=400,
    alpha=0.5,
    title='Custom Decision Boundary'
)
```

### 📌 Additional Options

* `class_names`: Use list or dict to assign labels
* Control `standardize`, `pca_components`, `figsize`, etc.
* Use `fit_model=False` if your model is already trained

---

## 🧾 API Reference

```python
plot_decision_boundary(
    model, X, y,
    class_names=None,
    standardize=True,
    pca_components=2,
    grid_resolution=300,
    padding=1.0,
    cmap_light=None,
    cmap_bold=None,
    alpha=0.3,
    title="Decision Boundary",
    fit_model=True,
    figsize=(8, 6),
    random_state=None
)
```

| Parameter         | Type       | Description                                  | Default               |
| ----------------- | ---------- | -------------------------------------------- | --------------------- |
| `model`           | estimator  | scikit-learn classifier (fitted or unfitted) | *Required*            |
| `X`               | array      | Feature matrix (n\_samples, n\_features)     | *Required*            |
| `y`               | array      | Class labels (n\_samples,)                   | *Required*            |
| `class_names`     | list/dict  | Optional class name labels                   | `None`                |
| `standardize`     | bool       | Whether to standardize features              | `True`                |
| `pca_components`  | int        | Number of PCA components (for high-dim data) | `2`                   |
| `grid_resolution` | int        | Grid density for the surface                 | `300`                 |
| `padding`         | float      | Padding around feature range                 | `1.0`                 |
| `cmap_light`      | cmap       | Colormap for decision surface                | `auto`                |
| `cmap_bold`       | list       | Colors for scatter points                    | `auto`                |
| `alpha`           | float      | Transparency of decision surface             | `0.3`                 |
| `title`           | str        | Plot title                                   | `"Decision Boundary"` |
| `fit_model`       | bool       | Whether to train model on X, y               | `True`                |
| `figsize`         | tuple      | Size of the figure                           | `(8, 6)`              |
| `random_state`    | int / None | PCA reproducibility                          | `None`                |

---

## 🧠 When to Use `decisioncanvas`

* 🔍 **Data Exploration**: Quickly check how your model separates classes
* 🐞 **Model Debugging**: Detect overfitting or data overlap
* 👨‍🏫 **Teaching/Training**: Make classifiers interpretable for learners
* 🧪 **Publications & Slides**: Clean plots ready for presentations

---

## 🤝 Contributing

We welcome contributions!

### To contribute:

1. **Fork** the repository
2. **Clone** your copy
3. Install dependencies:

```bash
pip install -e .
```

4. Add tests to `tests/` and examples to `examples/`
5. Submit a detailed pull request

---

## 📄 License

Licensed under the **MIT License** – free for all uses.

---

## 👤 Credits

Created and maintained by **\[Your Name]**
Feedback, issues, and collaboration are appreciated!

---

## 🔗 Useful Links

* 📦 PyPI: [https://pypi.org/project/decisioncanvas/](https://pypi.org/project/decisioncanvas/)
* 📁 Examples: See example notebooks in the `examples/` folder
* 🐛 Issues: \[Link to your GitHub repo's issues tab]

---

## ✅ Get Started Now

```bash
pip install decisioncanvas
```

```python
plot_decision_boundary(model, X, y)
```

> See your classifier’s decision boundary with a single line of code!

```

---

