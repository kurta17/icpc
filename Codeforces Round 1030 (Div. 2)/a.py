for _ in range(int(input())):
    n = int(input())
    a = input()
    k = int(input())
    b = input()
    c = input().strip()
    start = []
    end = ''

    for i in range(k):
        if c[i] == "V":
            start.append(b[i])
        else:
            end+=b[i]
    start.reverse()
    s = "".join(start)
    print(s+a+end)