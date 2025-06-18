import math
for _ in range(int(input())):
    n,m,a,b = map(int, input().split())
    y = min((b), (m-b+1))
    x = min((a), (n-a+1))

    print((1 + (min((math.ceil(math.log2(x)) + math.ceil(math.log2(m))), (math.ceil(math.log2(y)) + math.ceil(math.log2(n)))))))