def solve():
    n = int(input())
    a = list(map(int, input().split()))
    # Create list of (weight, position) pairs (1-based positions)
    buttons = [(a[i], i + 1) for i in range(n)]
    # Sort by weight in descending order
    buttons.sort(reverse=True)
    
    # Initialize answer with 1 clone for the first button
    ans = 1
    # Initialize segment with the first button's position
    min_pos = max_pos = buttons[0][1]
    
    # Process remaining buttons
    for i in range(1, n):
        p = buttons[i][1]  # Current button's position
        # If position is not adjacent to current segment, need a new clone
        if p != min_pos - 1 and p != max_pos + 1:
            ans += 1
        # Update segment
        min_pos = min(min_pos, p)
        max_pos = max(max_pos, p)
    
    print(ans)

# Read number of test cases
t = int(input())
# Process each test case
for _ in range(t):
    solve()