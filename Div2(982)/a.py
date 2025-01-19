for _ in range(int(input())):
    w = []
    h = []
    for _ in range(int(input())):
        a,b = map(int,input().split())
        w.append(a)
        h.append(b)
    ww = max(w)
    hh = max(h)
    print(2*ww + 2*hh)

