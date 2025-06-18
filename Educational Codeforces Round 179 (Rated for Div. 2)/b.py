fib = [1, 2]
for i in range(2, 11):
    fib.append(fib[-1] + fib[-2])

for _ in range(int(input())):
    n, m = map(int, input().split())
    mw = fib[n-1]
    mh = fib[n-1] + fib[n-2]
    ans = []
    for _ in range(m):
        d = list(map(int, input().split()))
        d.sort()
        if d[0] >= mw and d[1] >= mw and d[2] >= mh:
            ans.append("1")
        else:
            ans.append("0")
    print("".join(ans))