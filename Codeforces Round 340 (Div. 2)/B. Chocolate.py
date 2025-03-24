n = int(input())
a = list(map(int, input().split()))


firs1 = 0
last1 = 0

for i in range(n):
    if a[i] == 1:
        firs1 = i
        break

for i in range(n-1,-1,-1):
    if a[i] == 1:
        last1 = i
        break


bars = a[firs1:last1+1]

if 1 not in bars:
    print(0)
else:
    ans = 1
    zero_count = 0

    for i in range(1,len(bars)):
        if bars[i] == 0:
            zero_count += 1
        elif bars[i] == 1:
            ans *= (zero_count+1)
            zero_count = 0

    print(ans)