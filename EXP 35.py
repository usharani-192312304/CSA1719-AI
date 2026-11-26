
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Input training data
X = np.array([[1, 2], [2, 3], [3, 4],
              [6, 7], [7, 8], [8, 9]])

# Target classes
y = np.array([0, 0, 0, 1, 1, 1])

# Create Decision Tree model
model = DecisionTreeClassifier()

# Train the model
model.fit(X, y)

# Predict a new data
new_data = np.array([[2, 4]])
prediction = model.predict(new_data)

print("Decision Tree Classification")
print("Input Data:", new_data[0])
print("Predicted Class:", prediction[0])
