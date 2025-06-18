
s,s1,s2 = map(str, input().split())
n = int(s)
a = list(map(str, input().strip()))

for i in range(n):
    if a[i] != s1:
        a[i] = s2
print("".join(a))