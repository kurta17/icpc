t = int(input())
for _ in range(t):
    n = input()
    num = int(n, 2)

    mask = 1 << (len(n) - 1)
    res = num ^ mask
    res = bin(res)[2:]
    print(res)
    last_one_ind = res.rfind('0')

    if last_one_ind == -1:
        print(1,len(n),1,1)
    else:
        print(1,len(n),1,last_one_ind+1)

