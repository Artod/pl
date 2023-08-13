import random

def monte_carlo_pi(num_samples: int) -> float:
    """Estimate the value of π using a Monte Carlo method."""
    
    inside_circle = 0

    for _ in range(num_samples):
        x, y = random.random(), random.random()  # Random points between 0 and 1
        distance_to_origin = x**2 + y**2
        
        if distance_to_origin <= 1:
            inside_circle += 1

    # The area of the quarter circle (π/4) compared to the area of the unit square (1)
    # gives us the ratio of inside_circle to num_samples..
    return (inside_circle / num_samples) * 4

if __name__ == "__main__":
    num_samples = 100000
    estimated_pi = monte_carlo_pi(num_samples)
    print(f"Estimated value of π with {num_samples} samples: {estimated_pi}")

    with open("pi_estimate.txt", "w") as file:
        file.write(str(estimated_pi))
    