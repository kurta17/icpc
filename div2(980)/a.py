t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    if a >= b:
        print(a)
    else:
        diff = b - a
        if diff > a:
            print(0)
        else:
            a -= (diff)
            print(a)
            