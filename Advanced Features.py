import random

# Reproducible results with seeding
random.seed(42)  # Set seed for reproducibility
print(random.random())  # Will always be 0.6394267984578837 with seed 42

# System random (cryptographically secure)
secure_random = random.SystemRandom()
print(secure_random.random())  # Uses OS's random source
