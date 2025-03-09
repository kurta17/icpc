from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
d_a = defaultdict(int)
d_b = defaultdict(int)

for i in range(n):
    d_a[a[i]] = i
    d_b[b[i]] = i

shifts = defaultdict(int)
for i in range(n):
    curr = a[i]
    shift = d_b[curr] - d_a[curr]
    if shift < 0:
        shift += n
    shifts[shift] += 1

print(max(shifts.values()))
    

