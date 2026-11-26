
import random

# Define the fitness function
def fitness(x):
    return x * x

# Generate initial population
population = [random.randint(0, 31) for _ in range(6)]

# Genetic Algorithm
for generation in range(10):

    # Selection
    population.sort(key=fitness, reverse=True)
    parent1 = population[0]
    parent2 = population[1]

    # Crossover
    child = (parent1 + parent2) // 2

    # Mutation
    if random.random() < 0.2:
        child = random.randint(0, 31)

    # Update population
    population[-1] = child

    print("Generation", generation + 1,
          "Best Fitness:", fitness(max(population)))

# Display result
best = max(population, key=fitness)

print("\nOptimal Solution:", best)
print("Maximum Fitness:", fitness(best))
