from collections import defaultdict

s = input()

d = defaultdict(int)
for i in s:
    d[i] += 1

numb_of_odd = 0
for i in d.values():
    if i % 2 == 1:
        numb_of_odd += 1

if numb_of_odd == 0 or numb_of_odd % 2 != 0:
    print("First")
else:
    print("Second")