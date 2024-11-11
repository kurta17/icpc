d = {"A":1, "B":2, "C":4, "?": 0}

t = int(input())

for _ in range(t):
    s1 = input().strip()
    s2 = input().strip()
    s3 = input().strip()
    xor1 = 0
    xor2 = 0
    xor3 = 0

    for i in s1:
        xor1 ^= d[i]
    for i in s2:
        xor2 ^= d[i]
    for i in s3:
        xor3 ^= d[i]
    
    full = 7
    ans = ""
    for i in xor1,xor2,xor3:
        if i != full:
            k = {1: "A", 2: "B", 4: "C"}
            ans += k[full-i]

    print(ans)
