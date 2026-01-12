# Hierarchical Clustering

## Concept
Hierarchical clustering builds a hierarchy of clusters. It doesn't require pre-specifying the number of clusters.

## Key Terms
- **Model**: The algorithm trained on data.
- **Fit**: Training the model.
- **Predict**: Using the model to infer new data.

## Python Implementation via Scikit-Learn

```python
from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering()
cluster.fit_predict(X)
```
