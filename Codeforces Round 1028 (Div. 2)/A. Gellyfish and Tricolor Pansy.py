for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    g_m = min(a,c)
    f_m = min(b,d)
    if g_m >= f_m:
        print("Gellyfish")
    else:
        print("Flower")
    

