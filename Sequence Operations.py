import random

colors = ['red', 'green', 'blue', 'yellow']

# Choose a single random element
print(random.choice(colors))  # e.g., 'blue'

# Choose multiple unique elements (without replacement)
print(random.sample(colors, 2))  # e.g., ['yellow', 'red']

# Choose multiple elements (with possible replacement)
print(random.choices(colors, k=3))  # e.g., ['green', 'green', 'blue']

# Shuffle a list in place
random.shuffle(colors)
print(colors)  # e.g., ['yellow', 'blue', 'red', 'green']
