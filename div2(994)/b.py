from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    p = list(map(str, input().strip()))
    d = defaultdict(int)
    for i in p:
        d[i] += 1
    
    if (d['s'] == 0 or d['p'] == 0):
        print("YES")
    elif (p[-1] == 'p' and d['p'] == 1):
        print("YES")
    elif (p[0] == "s") and d['s'] == 1 :
        print("YES")
    elif d['.'] == n:
        print("YES")
    else:
        print('NO')
