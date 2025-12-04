from collections import defaultdict

for _ in range(int(input())):
    d = defaultdict(int)
    n,m = map(int, input().split())

    sets = []

    for j in range(n):        
        s = list(map(int, input().split()))
        for element in s[1:]:
            d[element] += 1
        sets.append(s)

    if len(d) < m:
        print('NO')
        continue

    d_need = 0

    for sett in sets:
        nums = 0
        for element in sett[1:]:
            if d[element] >1 :
                nums += 1
                if nums == sett[0]:
                    d_need += 1

        if d_need == 2:
            break
    
    print("YES" if d_need > 1 else "NO")