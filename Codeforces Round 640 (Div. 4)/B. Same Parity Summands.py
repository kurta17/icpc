for _ in range(int(input())):
    n,k = (map(int, input().split()))
    a = 2 if n % 2 == 0 and k % 2 == 1 else 1
    kminus1 = a * (k - 1)
    last = n - kminus1
    if last > 0 and last % 2 == a % 2:
        print("YES")
        print(*([a]*(k-1)),last)
    else:
        print("NO")
