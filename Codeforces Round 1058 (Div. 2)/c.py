for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print("YES")
        continue
    b = bin(n)[2:]
    i = len(b) - 1
    while b[i] == "0": i -= 1
    b = b[:i+1]
    if len(b) < 2:
        print("NO")
        continue
    # print(b)
    p = 0
    q = len(b) - 1
    ans = True
    while p < q:
        if b[p] != b[q]: ans = False
        p+=1
        q-=1
    # print(ans)
    if ans:
        if (len(b) % 2 != 0 and b[len(b)//2] != '0'):
            print("NO")
            # print(len(b),b[len(b)//2])
        else:
            print("YES")
    else:
        print("NO")

