import os
import math
import numpy as np
import random
from typing import List, Tuple, Dict
from pathlib import Path

# Constants
PI = math.pi
TWO_PI = 2 * PI
EPSILON = 1e-6

def angle_diff(x: float, y: float) -> float:
    """Compute the smallest angle difference between x and y in [0, 2π)."""
    d = abs(x - y) % TWO_PI
    return min(d, TWO_PI - d)

def transition_cost(config1: List[float], config2: List[float]) -> float:
    """Compute the transition cost as max angle difference across segments."""
    return max(angle_diff(a, b) for a, b in zip(config1, config2))

def forward_kinematics(k: int, lengths: List[float], angles: List[float]) -> Tuple[float, float]:
    """Compute the (x, y) position of the arm's tip given angles and lengths."""
    x, y = 0.0, 0.0
    theta_sum = 0.0
    for i in range(k):
        theta_sum += angles[i]
        x += lengths[i] * math.cos(theta_sum)
        y += lengths[i] * math.sin(theta_sum)
    return x, y

def inverse_kinematics_2d(x: float, y: float, l1: float, l2: float) -> List[List[float]]:
    """Compute possible configurations for k=2 to reach (x, y)."""
    configs = []
    r_sq = x**2 + y**2
    r = math.sqrt(r_sq)
    
    # Check reachability
    if r > l1 + l2 + EPSILON or r < abs(l1 - l2) - EPSILON:
        # Point is unreachable - outside the workspace
        return configs
    
    c = (l1**2 + r_sq - l2**2) / (2 * l1 * r)
    # Handle numerical precision
    c = max(-1.0, min(1.0, c))  # Clamp to [-1, 1]
    
    phi = math.atan2(y, x)
    if phi < 0:
        phi += TWO_PI
    
    # Two solutions for theta1
    try:
        delta = math.acos(c)
        for sign in [1, -1]:
            theta1 = (phi + sign * delta) % TWO_PI
            x1 = l1 * math.cos(theta1)
            y1 = l1 * math.sin(theta1)
            theta_sum = math.atan2(y - y1, x - x1)
            if theta_sum < 0:
                theta_sum += TWO_PI
            theta2 = (theta_sum - theta1) % TWO_PI
            config = [theta1, theta2]
            # Verify the configuration
            x_tip, y_tip = forward_kinematics(2, [l1, l2], config)
            if abs(x_tip - x) <= EPSILON and abs(y_tip - y) <= EPSILON:
                configs.append(config)
    except ValueError:
        # This should not happen with the clamping above, but just in case
        pass
    
    return configs

def inverse_kinematics_3d(x: float, y: float, l1: float, l2: float, l3: float) -> List[List[float]]:
    """Compute configurations for k=3 to reach (x, y)."""
    configs = []
    
    # Check if point is potentially reachable
    r = math.sqrt(x**2 + y**2)
    if r > l1 + l2 + l3 + EPSILON:
        # Point is definitely unreachable
        return configs
    
    # Try more angles for better coverage - increased from 8 to 16 samples
    num_samples = 16
    theta3_values = [i * TWO_PI / num_samples for i in range(num_samples)]
    
    for theta3 in theta3_values:
        # Adjust target for the third segment
        x_adj = x - l3 * math.cos(theta3)
        y_adj = y - l3 * math.sin(theta3)
        configs_2d = inverse_kinematics_2d(x_adj, y_adj, l1, l2)
        
        for theta1, theta2 in configs_2d:
            config = [theta1, theta2, theta3]
            x_tip, y_tip = forward_kinematics(3, [l1, l2, l3], config)
            if abs(x_tip - x) <= EPSILON and abs(y_tip - y) <= EPSILON:
                configs.append(config)
    
    # If no configurations found, try numerical optimization
    if not configs and r <= l1 + l2 + l3:
        configs.extend(inverse_kinematics_numerical(3, [l1, l2, l3], x, y))
    
    return configs

def inverse_kinematics_numerical(k: int, lengths: List[float], target_x: float, target_y: float) -> List[List[float]]:
    """Use numerical optimization to find configurations."""
    configs = []
    max_attempts = 5
    
    for _ in range(max_attempts):
        # Start with random angles
        angles = [random.uniform(0, TWO_PI) for _ in range(k)]
        learning_rate = 0.01
        max_iterations = 500
        
        for iteration in range(max_iterations):
            x, y = forward_kinematics(k, lengths, angles)
            error = math.sqrt((x - target_x)**2 + (y - target_y)**2)
            
            if error < EPSILON:
                # Normalize angles to [0, 2π)
                angles = [angle % TWO_PI for angle in angles]
                configs.append(angles)
                break
                
            # Compute gradient numerically
            gradients = []
            for i in range(k):
                angles[i] += EPSILON
                x_plus, y_plus = forward_kinematics(k, lengths, angles)
                angles[i] -= EPSILON
                
                dx_dtheta = (x_plus - x) / EPSILON
                dy_dtheta = (y_plus - y) / EPSILON
                
                # Gradient points toward increasing error, so negate it
                gradient = -2 * ((x - target_x) * dx_dtheta + (y - target_y) * dy_dtheta)
                gradients.append(gradient)
            
            # Update angles
            for i in range(k):
                angles[i] = (angles[i] + learning_rate * gradients[i])
            
            # Adaptive learning rate
            if iteration % 100 == 0 and iteration > 0:
                learning_rate *= 0.5
    
    return configs

def find_closest_reachable_point(x: float, y: float, lengths: List[float]) -> Tuple[float, float]:
    """Find the closest reachable point to (x, y) if the point is unreachable."""
    total_length = sum(lengths)
    r = math.sqrt(x**2 + y**2)
    
    if r <= total_length:
        return x, y  # Point is already reachable
    
    # Scale down to maximum reach
    scale = total_length / r
    return x * scale, y * scale

def compute_configurations(k: int, lengths: List[float], strawberries: List[Tuple[float, float]]) -> List[List[List[float]]]:
    """Compute all possible configurations for each strawberry."""
    all_configs = []
    for i, (x, y) in enumerate(strawberries):
        if k == 2:
            configs = inverse_kinematics_2d(x, y, lengths[0], lengths[1])
        else:  # k == 3
            configs = inverse_kinematics_3d(x, y, lengths[0], lengths[1], lengths[2])
        
        # If no configurations found, try with closest reachable point
        if not configs:
            x_adj, y_adj = find_closest_reachable_point(x, y, lengths)
            if x_adj != x or y_adj != y:  # Only if point was adjusted
                if k == 2:
                    configs = inverse_kinematics_2d(x_adj, y_adj, lengths[0], lengths[1])
                else:  # k == 3
                    configs = inverse_kinematics_3d(x_adj, y_adj, lengths[0], lengths[1], lengths[2])
                if configs:
                    print(f"Warning: Strawberry {i+1} at ({x}, {y}) was adjusted to reachable point ({x_adj}, {y_adj})")
                else:
                    print(f"Warning: No valid configuration for strawberry at ({x}, {y})")
            else:
                print(f"Warning: No valid configuration for strawberry at ({x}, {y})")
        
        all_configs.append(configs)
    return all_configs

def nearest_neighbor_tsp(n: int, all_configs: List[List[List[float]]], initial_config: List[float]) -> Tuple[List[int], List[List[float]]]:
    """Find a painting order and configurations using nearest neighbor heuristic."""
    visited = [False] * n
    order = []
    configs = []
    current_config = initial_config
    visited_count = 0
    
    # Start with the strawberry closest to initial_config
    min_cost = float('inf')
    best_idx = -1
    best_config = None
    for i in range(n):
        if not visited[i] and all_configs[i]:  # Check that configs exist
            for config in all_configs[i]:
                cost = transition_cost(current_config, config)
                if cost < min_cost:
                    min_cost = cost
                    best_idx = i
                    best_config = config
    
    if best_idx == -1:
        return [], []
    
    order.append(best_idx + 1)  # 1-based indexing
    configs.append(best_config)
    visited[best_idx] = True
    visited_count += 1
    current_config = best_config
    
    # Continue with nearest unvisited strawberry
    while visited_count < n:
        min_cost = float('inf')
        best_idx = -1
        best_config = None
        for i in range(n):
            if not visited[i] and all_configs[i]:  # Check that configs exist
                for config in all_configs[i]:
                    cost = transition_cost(current_config, config)
                    if cost < min_cost:
                        min_cost = cost
                        best_idx = i
                        best_config = config
        if best_idx == -1:
            break
        order.append(best_idx + 1)
        configs.append(best_config)
        visited[best_idx] = True
        visited_count += 1
        current_config = best_config
    
    return order, configs

def two_opt_optimize(n: int, order: List[int], configs: List[List[float]], all_configs: List[List[List[float]]], initial_config: List[float]) -> Tuple[List[int], List[List[float]]]:
    """Apply 2-opt optimization to improve the TSP tour."""
    best_order = order[:]
    best_configs = configs[:]
    improved = True
    total_cost = compute_total_cost(best_order, best_configs, all_configs, initial_config)
    
    while improved:
        improved = False
        for i in range(1, n-1):
            for j in range(i+1, n):
                # Try reversing segment from i to j
                new_order = best_order[:i] + best_order[i:j+1][::-1] + best_order[j+1:]
                # Recompute configurations for new order
                new_configs = []
                current_config = initial_config
                valid = True
                for idx in new_order:
                    strawberry_idx = idx - 1
                    min_cost = float('inf')
                    best_config = None
                    for config in all_configs[strawberry_idx]:
                        cost = transition_cost(current_config, config)
                        if cost < min_cost:
                            min_cost = cost
                            best_config = config
                    if best_config is None:
                        valid = False
                        break
                    new_configs.append(best_config)
                    current_config = best_config
                if not valid:
                    continue
                new_cost = compute_total_cost(new_order, new_configs, all_configs, initial_config)
                if new_cost < total_cost:
                    best_order = new_order
                    best_configs = new_configs
                    total_cost = new_cost
                    improved = True
    return best_order, best_configs

def compute_total_cost(order: List[int], configs: List[List[float]], all_configs: List[List[List[float]]], initial_config: List[float]) -> float:
    """Compute total transition cost for a given order and configurations."""
    total = transition_cost(initial_config, configs[0])
    for i in range(len(order)-1):
        total += transition_cost(configs[i], configs[i+1])
    return total

def process_test_case(input_file: str, output_file: str):
    """Process a single test case and write the output."""
    with open(input_file, 'r') as f:
        k = int(f.readline().strip())
        lengths = list(map(float, f.readline().strip().split()))
        n = int(f.readline().strip())
        strawberries = []
        for _ in range(n):
            x, y = map(float, f.readline().strip().split())
            strawberries.append((x, y))
    
    # Compute configurations
    all_configs = compute_configurations(k, lengths, strawberries)
    
    # Initial configuration
    initial_config = [0.0] * k
    
    # Find order and configurations
    order, configs = nearest_neighbor_tsp(n, all_configs, initial_config)
    
    # Optimize with 2-opt
    if order:  # Only optimize if we have a valid solution
        order, configs = two_opt_optimize(n, order, configs, all_configs, initial_config)
    
    # Write output
    with open(output_file, 'w') as f:
        for idx, config in zip(order, configs):
            f.write(f"{idx} {' '.join(map(str, config))}\n")


input_dir = "/Users/giorgikurtanidze/Documents/GitHub/icpc/Midnight Code Cup 2025/inputs"
output_dir = "./outputs"
# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Process each test case
for test_id in range(9, 13):
    input_file = os.path.join(input_dir, f"{test_id:02d}")
    print(f"Looking for input file: {input_file}")
    output_file = os.path.join(output_dir, f"{test_id:02d}.out")
    if os.path.exists(input_file):
        print(f"Processing test case {test_id:02d}...")
        process_test_case(input_file, output_file)
    else:
        print(f"Input file {input_file} not found, skipping.")