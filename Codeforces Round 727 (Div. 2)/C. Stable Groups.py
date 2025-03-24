n,k,x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
gaps = []
for i in range(1,n):
    if a[i] - a[i-1] > x:
        gaps.append(a[i] - a[i-1])

  
gaps.sort()
ans = len(gaps)
for i in range(ans):
    if k > 0:
        if gaps[i] % x == 0:
            if k - (gaps[i] // x) + 1 >= 0:
                k = k - (gaps[i] // x) + 1
                ans -= 1
        else:
            if k - gaps[i] // x >= 0:
                k -= gaps[i] // x
                ans -= 1

print(ans+1)


        



