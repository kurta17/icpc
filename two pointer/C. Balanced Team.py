n = int(input())
a = list(map(int,input().split()))

a.sort()
i = 0
j = 0
ans = 0

while j < n-1:
    ans = max(ans, j-i+1)
    if a[j+1] - a[i] <= 5:
        j+=1
    elif i == j:
        i += 1
        j += 1
    else:
        i += 1
    

ans = max(ans, j-i+1)

print(ans)
