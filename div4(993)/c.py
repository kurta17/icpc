t = int(input())

for _ in range(t):
    m,a,b,c = map(int, input().split())
    
    pirveli = min(m, a)
    meore = min(m, b)
    c = min(c, 2 * m - (pirveli + meore))
    print(pirveli+meore+c)



