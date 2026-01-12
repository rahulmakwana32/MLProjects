# Random Forest

## Concept
Random Forest is an ensemble method that fits multiple decision trees on various sub-samples of the dataset and uses averaging to improve predictive accuracy.

## Key Terms
- **Model**: The algorithm trained on data.
- **Fit**: Training the model.
- **Predict**: Using the model to infer new data.

## Python Implementation via Scikit-Learn

```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```
