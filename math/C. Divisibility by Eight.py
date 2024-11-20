n = str(input())
ans = -10000000000
for i in range(len(n)-1,-1,-1):
    if int(n[i]) % 2 == 0:
        last = n[i]
        for j in range(i-1,-1,-1):
            for k in range(j-1,-1,-1):
                if int(n[k] + n[j]+last) == 0 and k > 0:
                    ans = str(n[k-1]) + str(n[k]) + n[j] + last
                elif int(n[k] + n[j]+last) % 8 == 0:
                    ans = int(n[k] +n[j]+last)
                break
            
        


if ans == -10000000000:
    print("NO")
else:
    print('YES')
    print(ans)