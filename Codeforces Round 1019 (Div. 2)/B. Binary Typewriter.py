for _ in range(int(input())):
    n = int(input())
    a = input().strip()
    c = 0
    for i in range(1,n):
        if a[i] != a[i-1]:
            c += 1
            
    if c == 0:
        print(n + int(a[0] == "1"))
    elif c == 1:
        print(n + 1)
    else:
        print(n+c-1 - int(a[0] == "0" and c > 2))