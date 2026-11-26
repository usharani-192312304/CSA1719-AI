
import numpy as np
from sklearn.linear_model import LinearRegression

# Input training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([10, 20, 30, 40, 50])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict a continuous value
hours = np.array([[6]])
prediction = model.predict(hours)

print("Linear Regression Prediction")
print("Input Value:", hours[0][0])
print("Predicted Value:", prediction[0])
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
