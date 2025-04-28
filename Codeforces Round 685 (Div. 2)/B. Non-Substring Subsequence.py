for _ in range(int(input())):
    n, q = map(int, input().split())
    s = input().strip()
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1 
        ans = False
        for j in range(l):
            if s[j] == s[l]:
                ans = True
                break
        for j in range(r, n):
            if s[j] == s[r-1]: 
                ans = True
                break
        print("YES" if ans else "NO")