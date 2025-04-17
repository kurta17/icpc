# Generate 01.out - For solution 1
with open('01.out', 'w') as f:
    f.write('12\n')
    for _ in range(24):
        f.write('1 1\n')

# Generate 02.out - For solution 2
with open('02.out', 'w') as f:
    f.write('30\n')
    w, v = 1, 99
    while w < 10 and w*3 + v*2 <= 100:  # Ensure we stay within byte limit
        f.write(f'{w} {v}\n')
        w += 1
        v -= 1

# Generate 03.out - For solution 3
with open('03.out', 'w') as f:
    f.write('45\n')
    items = [(5, 13), (6, 15), (7, 16), (8, 18), (9, 20), 
             (10, 22), (11, 24), (12, 26), (13, 28)]
    
    bytes_used = 3  # For "45\n"
    for w, v in items:
        line = f'{w} {v}\n'
        bytes_used += len(line)
        if bytes_used <= 99:  # Keep under 100 bytes
            f.write(line)