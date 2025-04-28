for _ in range(int(input())):
    ll = int(input())
    n = (input())
    one = 0
    zero = 0
    for i in n:
        if i == '1':
            one+=1
        else:
            zero += 1
    print(one*(ll-1) + zero)

