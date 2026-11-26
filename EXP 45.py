import random

# Define the transition probabilities
transition_matrix = {
    'A': {'A': 0.2, 'B': 0.8},
    'B': {'A': 0.6, 'B': 0.4}
}

# Initial event
current_state = 'A'

print("Initial Event:", current_state)

# Predict the next 10 events
for i in range(10):
    states = list(transition_matrix[current_state].keys())
    probabilities = list(transition_matrix[current_state].values())

    next_state = random.choices(states, weights=probabilities)[0]

    print("Next Event:", next_state)
    current_state = next_state
