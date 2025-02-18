for _ in range(int(input())):
    a1,a2,a4,a5 = map(int,input().split())
    a3_1 = a1 + a2
    a3_2 = a4 - a2 
    a3_3 = a5 - a4

    if a3_1 == a3_2 == a3_3:
        print(3)
    elif a3_3 != a3_2 and a3_3 != a3_1 and a3_2 != a3_1:
        print(1)
    else:
        print(2)