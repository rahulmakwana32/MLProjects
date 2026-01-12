# Anomaly Detection

## Concept
Anomaly detection is the identification of rare items, events or observations which raise suspicions by differing significantly from the majority of the data.

## Key Terms
- **Model**: The algorithm trained on data.
- **Fit**: Training the model.
- **Predict**: Using the model to infer new data.

## Python Implementation via Scikit-Learn

```python
from sklearn.ensemble import IsolationForest
clf = IsolationForest()
clf.fit(X_train)
preds = clf.predict(X_test)
```
