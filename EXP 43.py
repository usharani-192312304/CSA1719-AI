
import numpy as np
import random

# Create Q-table
Q = np.zeros((5, 2))

# Learning parameters
alpha = 0.1
gamma = 0.9
epsilon = 0.2

# Training the agent
for episode in range(1000):
    state = 0

    while state != 4:

        # Choose action
        if random.random() < epsilon:
            action = random.randint(0, 1)
        else:
            action = np.argmax(Q[state])

        # Move left or right
        next_state = state + 1 if action == 1 else max(0, state - 1)

        # Reward for reaching goal
        reward = 10 if next_state == 4 else -1

        # Update Q-value
        Q[state, action] += alpha * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )

        state = next_state

# Display learned Q-table
print("Trained Q-Table:")
print(Q)

# Test the agent
state = 0
print("\nAgent Path:")

while state != 4:
    action = np.argmax(Q[state])
    state = state + 1 if action == 1 else max(0, state - 1)
    print(state)
