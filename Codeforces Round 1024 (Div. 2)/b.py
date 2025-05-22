for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    less = 0
    more = 0
    for i in range(1,n):
        if abs(a[i]) <= abs(a[0]):
            less += 1
        else:
            more += 1
    if less == more or less == more + 1 or more == n-1 or more == n-2:
        print("YES")
    else:
        print("NO")