t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    
    if '0' not in s:
        # Case: All '1's
        print(1, n, 1, 1)
        continue
    
    max_xor = 0
    result = (1, 1, 1, 1)
    
    # Iterate over all possible split points
    for i in range(1, n + 1):  # i is the end of the first substring
        for j in range(i + 1, n + 1 + 1):  # j is the end of the second substring
            a = int(s[:i], 2)  # First substring
            b = int(s[i:j], 2)  # Second substring
            current_xor = a ^ b
            if current_xor > max_xor:
                max_xor = current_xor
                result = (1, i, i + 1, j)
    
    print(*result)
