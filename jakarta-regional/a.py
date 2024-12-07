import math

vow = ["A","E","I","O","U"]
v = 0
c = 0
n = 0
g = 0
y = 0

s = input()

for i in s:
    if i in vow:
        v += 1
    elif i == "Y":
        y += 1
    elif i == "N":
        n += 1
    elif i == "G":
        g += 1
    else:
        c += 1

ans = 0

for ng_used in range(min(n,g)+1):
    rem_n = n - ng_used
    rem_g = g - ng_used

    cur_c = c + ng_used

    for y_vow in range(y + 1):
        y_con = y - y_vow

        tot_vow = v + y_vow
        tot_con = cur_c + y_con

        syl = min(tot_vow, tot_con//2)

        ans = max(ans,syl*3)

print(ans)

