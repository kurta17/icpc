n,s = map(int, input().split())
a = list(map(int, input().split()))

tot_s = sum(a)

b = a + a
pref_b = [0] * (2 * n + 1)
for i in range(2 * n):
    pref_b[i+1] = pref_b[i] + b[i]

ans = False
rem_s = s % tot_s
if rem_s == 0:  
    print("Yes")
    exit()

unique_sums = set(pref_b)

for i in range(2 * n + 1):
    if pref_b[i] + rem_s in unique_sums:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")
