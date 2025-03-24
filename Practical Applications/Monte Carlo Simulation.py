import random

def estimate_pi(n=1000000):
    inside = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside += 1
    return 4 * inside / n

print(estimate_pi())  # Approximates π
