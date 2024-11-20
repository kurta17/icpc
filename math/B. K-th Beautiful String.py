t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    ans = ["a"] * n

    for i in range(n-2,-1,-1):
        if k <= n-i-1:
            ans[i] = "b"
            ans[n-k] = "b"
            break
        k-= n-i-1
    print("".join(ans))


        