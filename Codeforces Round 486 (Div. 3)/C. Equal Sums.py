tr = []

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)

    for j in range(n):
        tr.append((s-a[j],i+1,j+1))

tr.sort(key = lambda x: x[0])

for i in range(1,len(tr)):
    if tr[i][0] == tr[i-1][0] and tr[i][1] != tr[i-1][1]:
        print("YES")
        print(tr[i][1], tr[i][2])
        print(tr[i-1][1], tr[i-1][2])
        break
else:
    print("NO")
 
