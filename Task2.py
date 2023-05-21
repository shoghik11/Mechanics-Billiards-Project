import numpy as np
import matplotlib.pyplot as plt


def next_position(x, y, px, py):
    # next position depending on path's intersection with circle 
    x_next = x + px
    # taken g = 10
    y_next = y + py - (10 * px**2)/2 

    return x_next, y_next


def next_momentum(x, y, px, py):
    # normalization by dividing vectors by their magnitude
    p_norm = np.hypot(px, py)  
    if p_norm > 0:
        px /= p_norm
        py /= p_norm

    px_new = (y**2 - x**2) * px - 2 * x * y * py
    py_new = -2 * x * y * px + (x**2 - y**2) * py

    return px_new, py_new

def calculate_deviation(x_traj, y_traj, x_rev_traj, y_rev_traj):
    deviations = np.sqrt((np.array(x_traj) - np.array(x_rev_traj))**2 + (np.array(y_traj) - np.array(y_rev_traj))**2)
    deviation = np.max(deviations)
    return deviation


def simulate_billiard(num_reflections, deviation_threshold):
    x_traj, y_traj, x_rev_traj, y_rev_traj = [], [], [], []
    
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    px = np.random.uniform(-1, 1)
    py = np.random.uniform(-1, 1)
    

    for _ in range(num_reflections):
        x_traj.append(x)
        y_traj.append(y)
        x_rev_traj.append(x)
        y_rev_traj.append(y)
        
        x, y = next_position(x, y, px, py)
        px, py = next_momentum(x, y, px, py)

    # reversing
    px = -px
    py = -py

    for _ in range(num_reflections):
        x_rev_traj.append(x)
        y_rev_traj.append(y)
        x, y = next_position(x, y, px, py)
        px, py = next_momentum(x, y, px, py)
        
    # deviation between the regular path and it's reverse
    deviation = calculate_deviation(x_traj, y_traj, x_rev_traj, y_rev_traj)
    if(deviation<0):
        deviation=0
  
    return deviation, x_traj, y_traj, x_rev_traj, y_rev_traj


def plot_billiard(x_traj, y_traj, x_rev_traj, y_rev_traj):
    fig, ax = plt.subplots(figsize=(8, 8))

    ax.plot(x_traj, y_traj, color='green', label='Original Motion')
    ax.plot(x_rev_traj, y_rev_traj, color='orange', label='Reversed Motion')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Mechanics: Vertical Circular Billiard')
    ax.legend()
    ax.grid(True)

    plt.show()

def check_deviation(num_reflections, deviation_threshold):
    deviation, x_traj, y_traj, x_rev_traj, y_rev_traj = simulate_billiard(num_reflections, deviation_threshold)

    if deviation > deviation_threshold:
        print(f"The paths deviate after {num_reflections} reflections.")
    else:
        print("The paths coincide.")

num_reflections = 10
deviation_threshold = 1e-6   

deviation, x_traj, y_traj, x_rev_traj, y_rev_traj = simulate_billiard(num_reflections, deviation_threshold)
if deviation > deviation_threshold:
    print(f"Deviate after {num_reflections} reflections.")
else:
    print("Same path.")
