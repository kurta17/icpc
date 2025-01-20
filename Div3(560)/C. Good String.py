n = int(input())
s = input().strip()

ans = []
i = 0

while i < n - 1:
    if s[i] != s[i + 1]:
        ans.append(s[i])
        ans.append(s[i + 1])
        i += 2
    else:
        i += 1

if len(ans) % 2 != 0:
    ans = ans[:-1]

print(n - len(ans))
print(''.join(ans))