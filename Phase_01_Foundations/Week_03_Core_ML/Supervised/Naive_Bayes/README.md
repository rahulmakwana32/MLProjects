# Naive Bayes

## Concept
Naive Bayes methods are a set of supervised learning algorithms based on applying Bayes' theorem with the 'naive' assumption of conditional independence between every pair of features.

## Key Terms
- **Model**: The algorithm trained on data.
- **Fit**: Training the model.
- **Predict**: Using the model to infer new data.

## Python Implementation via Scikit-Learn

```python
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```
