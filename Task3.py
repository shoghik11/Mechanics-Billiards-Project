import random
import math
import numpy as np


def simulate_stadium_billiard(L, n):
    r = 1 # Radius of circle
    x_left = 0  # left semicircle's center's x-coordinate 
    x_right = L  # right semicircle's center's y-coordinate 

    # Initialization
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    magnitude_p = 1
    theta = random.uniform(0, 2*math.pi)
    px = magnitude_p * math.cos(theta)
    py = magnitude_p * math.sin(theta)

    # reflection points
    reflection_points = [(x, y)]

    # Simulate the billiard motion
    while len(reflection_points) < n:
        # Cfinfing collision of particle
        if y < -r:  # Bottom line 
            # find intersection with bottom line segment
            intersection_x = x + (y + r) * px / py
            intersection_y = -r

            # find momentum after it
            ppx = px
            ppy = -py

        elif y > r:  # Top line 
        # find intersection with it
            intersection_x = x + (y - r) * px / py
            intersection_y = r

            # find momentum after it
            ppx = px
            ppy = -py
        elif x > x_right:  # Right semicircle
        # find intersection with bottom line segment
            intersection_x = x_right + math.sqrt(r**2 - (y - r)**2)
            intersection_y = y

            # find momentum after it
            dx = intersection_x - x_right
            dy = y - r
            ppx = px - 2 * dx * (dx*px + dy*py) / (dx**2 + dy**2)
            ppy = py - 2 * dy * (dx*px + dy*py) / (dx**2 + dy**2)
        elif x < x_left:  # Left semicircle
            # find intersection
            intersection_x = x_left - math.sqrt(r**2 - (y - r)**2)
            intersection_y = y

            # find momentum
            dx = intersection_x - x_left
            dy = y - r
            ppx = px - 2 * dx * (dx*px + dy*py) / (dx**2 + dy**2)
            ppy = py - 2 * dy * (dx*px + dy*py) / (dx**2 + dy**2)


        else:
            break

     
        reflection_points.append((intersection_x, intersection_y))

        # updating
        x = intersection_x
        y = intersection_y
        px = ppx
        py = ppy

    return reflection_points



def testing(M, num_samples, L):
    r = 1  # radius of circle

    # Initialize the bins
    bins = [0] * M

    # Simulating mothion 
    for _ in range(num_samples):
        # Initialize the position and momentum
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        px = 1
        py = 0

        # Simulate the billiard motion
        while True:
            # hits bottom?
            if py < 0:
                # find intersection
                intersection_x = x + r * px / abs(py)
                intersection_y = -r

                bin_index = int(intersection_x * M)

                bins[bin_index] += 1

                break

            # moving with momentum
            x += px
            y += py

            # inside it?
            if abs(x) <= L and abs(y) <= r:
                break

    return bins



n = 5  # number of reflections
L_values = [2, 4, 3]
M = 10  # Number of bins
num_samples = 10000  # number of random samples

for L in L_values:
    reflection_points = simulate_stadium_billiard(L)
    print(f"Reflection points when L = {L}:")
    for i, point in enumerate(reflection_points):
        print(f"Reflection point {i+1}: {point}")

    bins = testing(M, num_samples, L)
    mean_entries = np.mean(bins)
    variance_entries = np.var(bins)

    print(f"\n Bins when L = {L}:")
    print(bins)
    print("Mean entries:", mean_entries)
    print("Variance of entries:", variance_entries)

