import math

for _ in range(int(input())):
    n,d = map(int,input().split())
    ans = [1]
    if n >= 3 or d % 3 == 0:
        ans.append(3)
    if d == 5:
        ans.append(5)
    if d == 7 or (n >=3):
        ans.append(7)
    if n>=6 or d == 9 or (d % 3 == 0 and n >= 3):
        ans.append(9)
    print(*ans)
