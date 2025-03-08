import random

def logistic_growth(P0, r, K, time, lag_range, exp_range):
    lag_phase = random.randint(*lag_range)
    exp_phase = random.randint(*exp_range)

    population = []
    for t in range(time):
        if t < lag_phase:
            pop = P0  # Population stays constant in lag phase
        elif t < lag_phase + exp_phase:
            pop = population[-1] * (1 + r) if population else P0  # Exponential growth
        else:
            pop = population[-1] + r * population[-1] * (1 - population[-1] / K)  # Logistic growth
        population.append(min(pop, K))  # Ensure it does not exceed carrying capacity
    return population

# Example run
random.seed(1)  # Fixing seed for reproducibility
output = logistic_growth(P0=10, r=0.2, K=1000, time=20, lag_range=(2, 5), exp_range=(5, 10))

# Displaying output
for t, pop in enumerate(output):
    print(f"Time {t}: Population {pop:.2f}")
