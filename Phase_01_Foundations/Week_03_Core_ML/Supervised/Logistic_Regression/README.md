# Logistic Regression

## Concept
Logistic Regression is used for binary classification problems (e.g., Spam vs Ham). It maps predicted values to probabilities using the sigmoid function.

## Key Terms
- **Model**: The algorithm trained on data.
- **Fit**: Training the model.
- **Predict**: Using the model to infer new data.

## Python Implementation via Scikit-Learn

```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```
