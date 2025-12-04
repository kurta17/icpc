for _ in range(int(input())):
    n,k = map(int, input().split())
    pairs = []
    for _ in range(n):
        l,r,c = map(int, input().split())
        if c >= k:
            pairs.append((l,r,c))
    pairs.sort(key=lambda x: x[2]) 
    for l,r,c in pairs:
        if k >= l and k <= r:
            k = c
    print(k)
