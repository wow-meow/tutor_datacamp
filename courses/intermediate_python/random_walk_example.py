import numpy as np
import matplotlib.pyplot as plt


def random_walk(n_steps):
    """
    Perform a random walk for n_steps.
    Returns the position after each step.
    """
    # Set random seed for reproducibility
    np.random.seed(123)

    # Generate steps: -1 or 1 with equal probability
    steps = np.random.choice([-1, 1], size=n_steps)
    print(steps)

    # Calculate positions by taking cumulative sum of steps
    positions = np.cumsum(steps)
    print(positions)

    return positions


# Generate random walk with 100 steps
n_steps = 100
positions = random_walk(n_steps)

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(range(n_steps), positions, "b-")
plt.title("Random Walk")
plt.xlabel("Step Number")
plt.ylabel("Position")
plt.grid(True)
plt.show()

# Print final position
print(f"Final position after {n_steps} steps:", positions[-1])
