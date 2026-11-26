
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Input training data
X = np.array([[1, 2], [2, 3], [3, 4],
              [6, 7], [7, 8], [8, 9]])

y = np.array([0, 0, 0, 1, 1, 1])

# Create KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Train the model
model.fit(X, y)

# Predict the class
new_data = np.array([[2, 4]])
prediction = model.predict(new_data)

print("KNN Classification")
print("Input Data:", new_data[0])
print("Predicted Class:", prediction[0])
