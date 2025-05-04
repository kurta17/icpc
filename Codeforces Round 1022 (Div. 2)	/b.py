for _ in range(int(input())):
    n,x = map(int,input().split())
    s = str(bin(x))[2:]
    y = len(s)

    if n == 1 and x == 0:
        print(-1)
    elif (x == 1 and n % 2 == 0) or (x == 0 and n % 2 ==1):
        print(n+3)
    else:          
        ans = 0
        n_count = 0
        for i in range(y):
            if s[i] == '1':
                b_str = '1' + '0' * (y-i-1)
                ans += int(b_str, 2)
                n_count+=1

        if n_count < n:
            n_left = n - n_count
            ans += n_left
            if n_left % 2 == 1:
                ans +=1

        print(ans)
