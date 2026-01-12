# KNN

## Concept
K-Nearest Neighbors classifies a data point based on how its neighbors are classified.

## Key Terms
- **Model**: The algorithm trained on data.
- **Fit**: Training the model.
- **Predict**: Using the model to infer new data.

## Python Implementation via Scikit-Learn

```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```
