import numpy as np

def billiardSimulation(numOfReflections):
    # Initialization
    x = np.random.uniform(-5, 5)
    y = np.random.uniform(-5, 5)
    p_x = np.random.uniform(-5, 5)
    p_y = np.random.uniform(-5, 5)
    p_norm = np.sqrt(p_x**2 + p_y**2)
    p_x /= p_norm
    p_y /= p_norm

    reflection_points = np.zeros((numOfReflections, 2))
    
    for i in range(numOfReflections):
        #intersection with edges
        a = p_x**2 + p_y**2
        b = 2 * (x*p_x + y*p_y)
        c = x**2 + y**2 - 1
        discriminant = b**2 - 4*a*c

        #guarantee being in interior part
        if discriminant >= 0:
            t = (-b + np.sqrt(discriminant)) / (2*a)
            x_temp = x + t * p_x #stex
            y_temp = y + t * p_y

            reflection_points[i] = [x_temp, y_temp] #st

            # Calculate new momentum
            nx = x_temp
            ny = y_temp
            p_x = (ny**2 - nx**2) * p_x - 2 * nx * ny * p_y
            p_y = -2 * nx * ny * p_x + (nx**2 - ny**2) * p_y
            p_norm = np.sqrt(p_x**2 + p_y**2)
            p_x /= p_norm
            p_y /= p_norm

            # Position update
            x = x_temp
            y = y_temp
        else:
            # not intersecting
            continue

    return reflection_points


# Example usage
numOfReflections = 10
reflection_points = billiardSimulation(numOfReflections)
print(reflection_points)