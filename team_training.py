def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()  # Sort in ascending order
    
    ans = 0
    i = 0
    
    while i < n:
        # Calculate members needed for minimum value a[i]
        needed = (x + a[i] - 1) // a[i]  # Ceiling division
        
        # Check if we can form a team with current minimum
        if needed > n - i:  # Not enough members left
            break
            
        ans += 1  # Form a team
        i += needed  # Skip used members
    
    return ans

# Process test cases
for _ in range(int(input())):
    print(solve())
