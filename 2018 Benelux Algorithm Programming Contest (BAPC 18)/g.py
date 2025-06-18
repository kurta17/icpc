from collections import defaultdict
import math


n = int(input())
a = input()

i = 0
j = n - 1

while i < j:
    if a[i] != a[j]:
        break
    j -= 1

d = defaultdict(int)

curr = a[:j+1]

for p in curr:
    d[p] += 1

amin = d["A"] - a[:d["A"]].count('A')
bmin = d["B"] - a[:d["B"]].count('B')
cmin = d["C"] - a[:d["C"]].count('C')
an = amin
for i in range(d["A"],len(curr)):
    if a[i - d["A"]] == "A":
        amin += 1
    if a[i] == "A":
        amin -= 1
    an = min(an,amin)

bn = bmin
for i in range(d["B"],len(curr)):
    if a[i - d["B"]] == "B":
        bmin += 1
    if a[i] == "B":
        bmin -= 1
    bn = min(bn,bmin)

cn = cmin
for i in range(d["C"],len(curr)):
    if a[i - d["C"]] == "C":
        cmin += 1
    if a[i] == "C":
        cmin -= 1
    cn = min(cn,cmin)


print(an+bn+cn)




