for _ in range(int(input())):
    n,a,b,c = map(int, input().split())
    tot = a+b+c
    mot = n//tot
    darch = n%tot
    if darch == 0:
        print(3*mot)
    elif darch <= a:
        print(3*mot + 1)
    elif darch <= a+b:
        print(3*mot+2)
    else:
        print(3*mot+3)
    