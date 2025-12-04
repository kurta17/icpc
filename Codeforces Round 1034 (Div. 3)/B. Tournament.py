for _ in range(int(input())):
    n,j,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = a.copy()
    b.sort()
    if k == 1:
        if a[j-1] == b[-1]:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")