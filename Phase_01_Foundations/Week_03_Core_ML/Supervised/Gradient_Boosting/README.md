# Gradient Boosting

## Concept
Gradient Boosting produces a prediction model in the form of an ensemble of weak prediction models, typically decision trees.

## Key Terms
- **Model**: The algorithm trained on data.
- **Fit**: Training the model.
- **Predict**: Using the model to infer new data.

## Python Implementation via Scikit-Learn

```python
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```
