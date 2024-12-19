import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    un_used = set(range(1, n + 1))
    
    ans = []
    for i in a:
        if i in un_used:
            ans.append(i)
            un_used.remove(i)
        else:
            ans.append(un_used.pop())
    print(*ans)

