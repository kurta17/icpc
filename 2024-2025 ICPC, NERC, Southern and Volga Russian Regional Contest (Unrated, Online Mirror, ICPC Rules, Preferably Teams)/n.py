t = int(input())

for _ in range(t):
    a,s,b = (map(str, input().strip()))
    a,b = int(a),int(b)
    if a > b:
        print(f"{a}>{b}")
    elif a == b:
        print(f"{a}={b}")
    else:    
        print(f"{a}<{b}")
        