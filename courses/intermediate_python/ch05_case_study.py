#!/usr/bin/env python3

""" Chapter 5. Case Study: Hacker Statistics
"""

import numpy as np

random_float = np.random.rand()  # Pseudo-random float number between 0 and 1

np.random.seed(123)  # Starting from a seed
# Array of 5 pseudo-random float numbers between 0 and 1
randArr1 = np.random.rand(5)
np.random.seed(123)  # Starting from a seed
# Array of 5 pseudo-random float numbers between 0 and 1
randArr2 = np.random.rand(5)
# ReSeeding ensures reproducibility
print(f"Diff of two random arrays: {randArr1 - randArr2}")
assert np.array_equal(randArr1, randArr2)

# [lb, ub) half-open interval --> generates 0 or 1
coin = np.random.randint(0, 2)
print(coin)
if coin == 0:
    print("head")
else:
    print("tail")

# Use randint() with the appropriate arguments to randomly generate the
# integer 1, 2, 3, 4, 5 or 6. This simulates a dice. Print it out.
np.random.seed(123)
dice = np.random.randint(1, 7)
print(dice)
# Repeat the outcome to see if the second throw is different. Again, print out the result.
dice = np.random.randint(1, 7)
print(dice)

# Current step
step = 50
# Roll the dice. Use randint() to create the variable dice.
np.random.seed(123)
dice = np.random.randint(1, 7)
# Finish the if-elif-else construct by replacing ___:
# If dice is 1 or 2, you go one step down.
# if dice is 3, 4 or 5, you go one step up.
# Else, you throw the dice again. The number on the dice is the number of steps you go up.
if dice <= 2:
    step -= 1
elif dice > 2 and dice < 6:
    step += 1
else:
    dice2 = np.random.randint(1, 7)
    print(f"Bonus! dice again: {dice2}")
    step += dice2
# Pint out dice and step. Given the value of dice, was step updated correctly?
print(f"dice = {dice} --> step = {step}")

# Create a random walk by adding a series of random steps
steps = []  # empty list
tails = [0]
print(len(tails))
np.random.seed(123)
for i in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[i] + coin)
    print(tails)
    if coin == 0:
        steps.append("head")
    elif coin == 1:
        steps.append("tail")
print(steps)
print(len(steps))
print(tails)
print(len(tails))

n_steps = 10
np.random.seed(123)
steps = np.random.choice([0, 1], size=n_steps)
# Create numpy array with multiple empty strings
outcomes_2 = np.array(
    [""] * n_steps, dtype="U4"
)  # U4 allows strings up to 4 characters
outcomes_2[steps == 0] = "head"
outcomes_2[steps == 1] = "tail"
tails_2 = np.cumsum(steps)
print(outcomes_2)
print(tails_2)

# Make a list random_walk that contains the first step, which is the integer 0.
positions = [0]

# Finish the for loop:
# The loop should run 100 times.
# On each iteration, set step equal to the last element in the random_walk list. You can use the index -1 for this.
# Next, let the if-elif-else construct update step for you.
np.random.seed(123)
n_steps = 100
for x in range(n_steps):
    # Set step: last element in random_walk
    step = positions[-1]

    # Roll the dice
    dice = np.random.randint(1, 7)

    # Determine the next step
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step += 1
    else:
        dice_again = np.random.randint(1, 7)
        step += dice_again

    # Append next step to random_walk
    positions.append(step)

# Print out random_walk.
positions.pop(0)
print(positions)

import matplotlib.pyplot as plt

# Use plt.plot() to plot random_walk.
plt.plot(range(n_steps), positions)
# Finish off with plt.show() to actually display the plot.
plt.show()


# Simulate the distribution of the occureances of the coin tail in 10 tosses of coins
n_games = 10000
n_tosses_per_game = 10
final_tails = []
np.random.seed(111)
for i in range(n_games):
    tails = [0]
    for j in range(n_tosses_per_game):
        coin = np.random.randint(0, 2)
        tails.append(tails[-1] + coin)
    final_tails.append(tails[-1])

print(f"min: {np.min(final_tails)}, max: {np.max(final_tails)}")
print

# Histogram
n_bins = 1 + n_tosses_per_game
plt.hist(final_tails, bins=n_bins)
plt.show()

# Create a sample array
# arr1 = np.array([1, 2, 3, 2, 1, 2, 4, 2, 5, 10, 10, 10, 0, 10])
arr1 = np.array(range(11))
n_bins = 1 + arr1.max() - arr1.min()
counts, bins, _ = plt.hist(arr1, bins=n_bins)
print("\nBin edges:", bins)
print("Counts in each bin:", counts)
plt.show()

# Method 1: np.count_nonzero()
count_value_equal_to_two = np.count_nonzero(arr1 == 2)
print("Count of 2 using count_nonzero():", count_value_equal_to_two)
# Method 2: np.sum() with boolean condition
count_2_sum = np.sum(arr1 == 2)
print("Count of 2 using sum():", count_2_sum)
# Works with strings too
str_arr = np.array(["head", "tail", "head", "head", "tail"])
count_head = np.count_nonzero(str_arr == "head")
print("Count of 'head':", count_head)


def roll_dice_n_walk(n_steps, init_position):
    positions = [init_position]
    for x in range(n_steps):
        if np.random.rand() < 0.005:
            position = 0
        else:
            position = positions[-1]
            dice = np.random.randint(1, 7)
            if dice <= 2:
                position = max(0, position - 1)
            elif dice <= 5:
                position = position + 1
            else:
                position = position + np.random.randint(1, 7)

        positions.append(position)

    return positions


# Initialize all_walks (don't change this line)
all_positions = []
np.random.seed(123)
# Simulate random walk multiple times
n_walks = 5000
for x in range(n_walks):
    positions = roll_dice_n_walk(100, 0)
    all_positions.append(positions)
#print(all_positions[-1])

# Use np.array() to convert all_walks to a NumPy array, np_aw.
np_aw = np.array(all_positions)
# Try to use plt.plot() on np_aw. Also include plt.show(). Does it work out of the box?
# plt.plot(np_aw)
# plt.show()

# Transpose np_aw by calling np.transpose() on np_aw. Call the result np_aw_t.
# Now every row in np_all_walks represents the position after 1 throw for the five random walks.
np_aw_t = np.transpose(np_aw)
# Use plt.plot() to plot np_aw_t; also include a plt.show(). Does it look better this time?
#plt.clf()
#plt.plot(np_aw_t)
#plt.show()

endpnts_walks = np_aw_t[-1, :]
plt.clf()
counts, bins, _ = plt.hist(endpnts_walks)
plt.show()

prob_over_60 = np.count_nonzero(endpnts_walks >= 60) / len(endpnts_walks)