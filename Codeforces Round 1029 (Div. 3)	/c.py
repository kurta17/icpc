import sys
input = sys.stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    prev = set()
    curr = set()
    i = 0
    for i in a:
        prev.add(i)
        curr.add(i)
        if len(prev) == len(curr):
            ans += 1
            curr.clear()
    print(ans)