n,k = map(int,input().split())
s = list(map(str, input().strip()))
a = list(input().split())

ans = 0
i = 0
j = 0

while i < n:
    curr = 0
    while j < n and s[j] in a:
        j += 1
        curr += 1
    ans += curr*(curr+1)//2
    i = j
    j += 1

print(ans)