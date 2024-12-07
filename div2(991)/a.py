t = int(input())

for _ in range(t):
    n,m = (map(int, input().split()))
    lengths = []
    for _ in range(n):
        s = input()
        lengths.append(len(s))
        
    ans = 0
    i = 0
    while m >= 0 and  i < len(lengths):
        m -= lengths[i]
        if m >= 0:
            ans += 1

        i+=1

    print(ans)

