# PCA

## Concept
Principal Component Analysis (PCA) is a technique for dimensionality reduction that increases interpretability but at the same time minimizes information loss.

## Key Terms
- **Model**: The algorithm trained on data.
- **Fit**: Training the model.
- **Predict**: Using the model to infer new data.

## Python Implementation via Scikit-Learn

```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(X)
X_pca = pca.transform(X)
```
