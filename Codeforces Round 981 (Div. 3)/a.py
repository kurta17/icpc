t = int(input())

for _ in range(t):
    n = int(input())
    x = 0
    ans = 0
    for i in range(2*n):
        if abs(x) > n:
            ans = i
            break
        elif i % 2 == 0:
            x -= (2*i + 1)
        else:
            x += (2*i + 1)
    if ans % 2 == 0:
        print("Kosuke")
    else:
        print("Sakurako")
