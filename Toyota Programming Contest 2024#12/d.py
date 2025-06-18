n,s = map(int, input().split())
a = list(map(int, input().split()))

tot_s = sum(a)

b = a + a
pref_b = [0] * (2 * n + 1)
for i in range(2 * n):
    pref_b[i+1] = pref_b[i] + b[i]

rem_s = s % tot_s
ans = False

i = 0
j = 2*n
while i < j:
    if (pref_b[j] - pref_b[i]) == rem_s or pref_b[i] == rem_s or pref_b[j] == rem_s:
        ans = True
        break
    
    if pref_b[j] - pref_b[i] < rem_s:
        j -= 1
    else:
        i += 1
if ans:
    print("YES")
else:
    print("NO")
