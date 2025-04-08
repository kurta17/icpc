for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    odds = []
    evens = []

    for i in range(n):
        if a[i] % 2 == 0:
            evens.append(a[i])
        else:
            odds.append(a[i])

    if len(odds) == 0:
        print(max(evens))
    elif len(evens) == 0:
        print(max(odds))
    else:
        print(sum(evens)+ sum(odds) - len(odds)+1)
