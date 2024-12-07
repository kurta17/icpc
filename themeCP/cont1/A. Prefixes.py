n = int(input())
s = (input())
ans = 0
res = []
for i in range(0,n,2):
    if 'ab' != s[i:i+2] and 'ba' != s[i:i+2]:
        res.append('ab')
        ans += 1
    else:
        res.append(s[i:i+2])

print(ans)
print(''.join(res))