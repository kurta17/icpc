t = int(input())
for _ in range(t):
    n = int(input())
    x,y = (map(int, input().split()))
    a = min(x,y)
    b = n // a
    if n % a == 0:
        print(b)
    else:
        print(b+1)
    