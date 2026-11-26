import numpy as np
import random

# XOR input and output
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Neural network prediction
def predict(weights):
    w1 = weights[:4].reshape(2, 2)
    b1 = weights[4:6].reshape(1, 2)
    w2 = weights[6:8].reshape(2, 1)
    b2 = weights[8]

    hidden = np.tanh(np.dot(X, w1) + b1)
    output = 1 / (1 + np.exp(-np.dot(hidden, w2) - b2))
    return output

# Fitness function
def fitness(weights):
    output = predict(weights)
    error = np.mean((y - output) ** 2)
    return 1 / (1 + error)

# Initialize population
population = [
    np.random.uniform(-2, 2, 9) for _ in range(30)
]

# Genetic Algorithm
for generation in range(1000):
    population.sort(key=fitness, reverse=True)

    if fitness(population[0]) > 0.99:
        break

    new_population = population[:2]

    while len(new_population) < 30:
        parent1, parent2 = random.choices(population[:10], k=2)

        # Crossover
        point = random.randint(1, 8)
        child = np.concatenate((
            parent1[:point], parent2[point:]
        ))

        # Mutation
        if random.random() < 0.2:
            index = random.randint(0, 8)
            child[index] += np.random.normal(0, 0.5)

        new_population.append(child)

    population = new_population

# Display results
best = max(population, key=fitness)

print("Best Fitness:", round(fitness(best), 4))
print("\nXOR Predictions:")

for i, prediction in enumerate(predict(best)):
    print(X[i], "->", round(float(prediction[0]), 2))
