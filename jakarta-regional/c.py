s = input()
t = input()

pref = {}
suff = {}

for i in range(1,len(s)):
    ch = s[i]
    if ch not in pref:
        pref[ch] = i

for i in range(len(t)-2,-1,-1):
    ch = t[i]
    if ch not in suff:
        suff[ch] = i

ans = 10**10
res = ""

for i in pref:
    if i in suff:
        ind1 = pref[i]
        ind2 = suff[i]
        l = ind1 + 2 + len(t) - ind2 
        if l < ans:
            ans = l
            res = s[:ind1] + t[ind2:]
            
if ans == 10**10:
    print(-1)
else:
    print(res)