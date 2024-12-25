
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    negone = 0
    posone = 0
    mm = 0
    for i in range(n):
        if a[i] == -1:
            negone+=1
        elif a[i] == 1:
            posone+=1
        else:
            mm = a[i]
    
    comb = [-i for i in range(1,negone+1)] + [0] + [j for j in range(1,posone+1)]
    for i in range(len(comb)):
        comb.append(comb[i] + mm)

    print(len(set(comb)))
    print(' '.join(map(str, sorted(set(comb)))))    

    
