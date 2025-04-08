for _ in range(int(input())):
    n = int(input())
    a = list(input().strip())
    b = list(input().strip())

    c_up_1_odd = 0
    c_dow_0_odd = 0
    c_up_1_even = 0
    c_dow_0_even = 0

    for i in range(n):
        if i % 2 == 0:
            if a[i] == '1':
                c_up_1_even += 1
            if b[i] == '0':
                c_dow_0_even += 1
        else:
            if a[i] == '1':
                c_up_1_odd += 1
            if b[i] == '0':
                c_dow_0_odd += 1

    # print(c_up_1_odd,c_dow_0_even)
    # print(c_up_1_even,c_dow_0_odd)

    if '1' not in a:
        print("YES")
    elif c_up_1_odd <= c_dow_0_even and c_up_1_even <= c_dow_0_odd:
        print("YES")
    else:
        print("NO")

