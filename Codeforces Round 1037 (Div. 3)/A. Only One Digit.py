for _ in range(int(input())):
    x = input()
    ans = float("inf")
    for i in x:
        ans = min(int(i), ans)
    print(ans)
