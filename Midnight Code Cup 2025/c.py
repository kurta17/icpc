import math

def forward_kinematics(theta, lengths):
    """Compute the (x, y) position of the arm's tip given angles and lengths."""
    x = 0
    y = 0
    angle_sum = 0
    for i in range(len(lengths)):
        angle_sum += theta[i]
        x += lengths[i] * math.cos(angle_sum)
        y += lengths[i] * math.sin(angle_sum)
    return x, y

def solve_2_segment(x, y, l1, l2):
    """Compute angles for a 2-segment arm to reach (x, y). Returns one solution."""
    d = math.sqrt(x**2 + y**2)
    # Handle edge case where d is very close to l1 + l2 or |l1 - l2|
    if abs(d - (l1 + l2)) < 1e-10 or abs(d - abs(l1 - l2)) < 1e-10:
        d += 1e-10  # Nudge to avoid numerical issues
    a = (l1**2 - l2**2 + d**2) / (2 * d)
    h = math.sqrt(l1**2 - a**2)  # Real since solution exists
    # Compute Joint 1 position (one solution: +h)
    px = a * x / d
    py = a * y / d
    vx = -y / d
    vy = x / d
    x1 = px + h * vx
    y1 = py + h * vy
    # Compute angles
    theta1 = math.atan2(y1, x1)
    if theta1 < 0:
        theta1 += 2 * math.pi
    theta2_raw = math.atan2(y - y1, x - x1) - theta1
    theta2 = theta2_raw % (2 * math.pi)
    return [theta1, theta2]

def solve_robot_arm(k, lengths, x, y):
    """Solve for angles to reach (x, y) with k segments."""
    if k == 2:
        return solve_2_segment(x, y, lengths[0], lengths[1])
    elif k == 3:
        # Set theta3 = 0, treat as 2-segment with l1 and l2 + l3
        theta12 = solve_2_segment(x, y, lengths[0], lengths[1] + lengths[2])
        return theta12 + [0.0]
    else:
        raise ValueError("k must be 2 or 3")

import os

def process_test_case(input_file, output_file):
    """Process a single test case from input_file and write the results to output_file."""
    try:
        with open(input_file, 'r') as infile:
            # Read input values
            k = int(infile.readline().strip())
            lengths = list(map(float, infile.readline().strip().split()))
            targets = []
            for line in infile:
                values = list(map(float, line.strip().split()))
                if len(values) == 1:
                    # If only one value is provided, assume y=0
                    targets.append([values[0], 0.0])
                elif len(values) == 2:
                    targets.append(values)
                else:
                    raise ValueError(f"Invalid target coordinates: {values} in {input_file}")

        # Validate input
        if len(lengths) != k:
            raise ValueError(f"Number of lengths ({len(lengths)}) does not match k ({k}) in {input_file}")

        # Solve for angles for each target
        results = []
        for target in targets:
            x, y = target
            angles = solve_robot_arm(k, lengths, x, y)
            if angles is not None:
                # Format angles with sufficient precision
                formatted_angles = [f"{angle:.8f}" for angle in angles]
                results.append(" ".join(formatted_angles))
            else:
                results.append("No solution found")

        # Write all results to the output file
        with open(output_file, 'w') as outfile:
            outfile.write("\n".join(results) + "\n")

    except Exception as e:
        print(f"Error processing {input_file}: {e}")

input_dir = "/Users/giorgikurtanidze/Documents/GitHub/icpc/Midnight Code Cup 2025/inputs"
output_dir = "./output"
print("hello")
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