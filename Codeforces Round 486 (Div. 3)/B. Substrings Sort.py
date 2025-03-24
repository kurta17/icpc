s = []
n = int(input())

for _ in range(n):
    s.append(input())

s.sort(key=len)
ans = True

for i in range(n-1):
    if s[i] not in s[i+1]:
        ans = False
        break
if not ans:
    print("NO")
else:
    print("YES")
    for i in range(n):
        print(s[i])
