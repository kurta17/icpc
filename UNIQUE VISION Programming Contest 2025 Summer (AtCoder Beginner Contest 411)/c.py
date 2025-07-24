n,q = map(int, input().split())
a = list(map(int, input().split()))

blacks = [False] * n
cur = 0
for i in range(q):
    ind = a[i] - 1
    blacks[ind] = not blacks[ind]
    # print(blacks)
    if blacks[ind]:
        if n == 1:
            cur += 1
            print(cur)
        elif (ind - 1 >= 0 and blacks[ind-1] == True) and (ind + 1 <= n-1 and blacks[ind+1] == True):
            cur-= 1
            print(cur)
        elif (ind - 1 >= 0 and blacks[ind-1] == False) and (ind + 1 <= n-1 and blacks[ind+1] == False):
            cur+= 1
            print(cur)
        elif (ind == 0 and blacks[1] == False) or (ind == n-1 and blacks[-2] == False):
            cur += 1
            print(cur)
        else:
            print(cur)
    else:
        if n == 1:
            cur -= 1
            print(cur)
        elif (ind - 1 >= 0 and blacks[ind-1] == True) and (ind + 1 <= n-1 and blacks[ind+1] == True):
            cur -= 1
            print(cur)
        elif (ind - 1 >= 0 and blacks[ind-1] == False) and (ind + 1 <= n-1 and blacks[ind+1] == False):
            cur -= 1
            print(cur)
        elif  (ind == 0 and blacks[1] == False) or (ind == n-1 and blacks[-2] == False):
            cur -= 1
            print(cur)
        else:
            print(cur)
