def time_to_80_percent(P0, r, K, time):
    population = P0
    for t in range(time):
        population += r * population * (1 - population / K)
        if population >= 0.8 * K:
            return t  # Return the time when 80% of K is reached
    return -1  # If not reached within given time

t_80 = time_to_80_percent(P0=10, r=0.2, K=1000, time=50)
print("Time to reach 80% of carrying capacity:", t_80)
