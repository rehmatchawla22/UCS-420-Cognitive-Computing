
import numpy as np

steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])

# a. Calculate total steps
total_steps = np.sum(steps)
print("Total steps:", total_steps)

# b. Calculate mean number of steps
mean_steps = np.mean(steps)
print("Mean steps:", mean_steps)

# c. Find maximum and minimum values
maximum = np.max(steps)
minimum = np.min(steps)

print("Maximum steps:", maximum)
print("Minimum steps:", minimum)

# d. Calculate total steps for each day using axis=0
daily_total = np.sum(steps, axis=0)
print("Total steps for each day:", daily_total)

# e. Calculate total steps for each user using axis=1
user_total = np.sum(steps, axis=1)
print("Total steps for each user:", user_total)

# f. Find position containing the maximum number of steps
max_position = np.unravel_index(np.argmax(steps), steps.shape)

print("Maximum value position:", max_position)
print("User index:", max_position[0])
print("Day index:", max_position[1])
