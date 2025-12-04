for _ in range(int(input())):
    n,k = map(int, input().split())
    s = input().strip()
    ans = ["+"] * n
    a = s.count('0')
    b = s.count('1')
    c = s.count('2')

    for i in range(n):
        if i < a or i >= n - b or n == k:
            ans[i] = "-"
        
        elif i < a + c or i >= n - b - c:
            ans[i] = "?"
        
    print(''.join(ans))


