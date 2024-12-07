t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if sum(a) % len(a) == 0:
        avv = sum(a) // len(a)
        for i in range(n-2):
            diff = a[i] - avv
            a[i+2] = a[i+2] + diff
            

        if a[-1] == avv and a[-2] == avv:
            print("YES")
        else:
            print("NO")

    else:
        print("NO")