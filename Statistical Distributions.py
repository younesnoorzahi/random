import random

# Normal distribution (Gaussian)
print(random.gauss(mu=0, sigma=1))  # e.g., 0.3293553302087163

# Exponential distribution
print(random.expovariate(lambd=1.5))  # e.g., 0.4379191155893253

# Triangular distribution
print(random.triangular(low=1, high=10, mode=5))  # e.g., 4.7234234234
