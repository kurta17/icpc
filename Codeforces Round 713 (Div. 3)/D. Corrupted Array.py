for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))

    b.sort()
    x = sum(b) - 2 * b[-1]
    if x in b[:-2]:
        b.remove(x)
        print(*b[:-1])
    elif sum(b[:-2]) == b[-2]:
        print(*b[:-2])
    else:    
        print(-1)
