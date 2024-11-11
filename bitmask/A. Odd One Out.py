t = int(input())

for _ in range(t):
    a,b,c = map(int,input().split())
    ans = 0

    for i in a,b,c:
        ans ^= i
    print(ans)