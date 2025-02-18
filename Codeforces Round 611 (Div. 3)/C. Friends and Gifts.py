n = int(input())
a = list(map(int, input().split()))

dontknow = []
unassigned = set(range(1, n+1))

for i in range(n):
    if a[i] == 0:
        dontknow.append(i+1)
    else:
        unassigned.discard(a[i])
print(unassigned)
print(dontknow)

for i in dontknow:
    print(list(unassigned)[0])
    if i == list(unassigned)[0]:
        a[i-1] = list(unassigned)[1]
        unassigned.discard(list(unassigned)[1])
    else:
        a[i-1] = list(unassigned)[0]
        unassigned.discard(list(unassigned)[0])
print(*a)
    



