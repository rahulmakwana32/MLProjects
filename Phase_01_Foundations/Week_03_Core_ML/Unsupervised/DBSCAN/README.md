# DBSCAN

## Concept
DBSCAN (Density-Based Spatial Clustering of Applications with Noise) finds core samples of high density and expands clusters from them.

## Key Terms
- **Model**: The algorithm trained on data.
- **Fit**: Training the model.
- **Predict**: Using the model to infer new data.

## Python Implementation via Scikit-Learn

```python
from sklearn.cluster import DBSCAN
model = DBSCAN(eps=3, min_samples=2)
model.fit(X)
```
