# SVM

## Concept
Support Vector Machines (SVM) find the hyperplane that best separates the classes in the feature space.

## Key Terms
- **Model**: The algorithm trained on data.
- **Fit**: Training the model.
- **Predict**: Using the model to infer new data.

## Python Implementation via Scikit-Learn

```python
from sklearn import svm
model = svm.SVC()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```
