for _ in range(int(input())):
    a,b,c = map(int,input().split())
    s = a + b + c
    if s % 3 == 0 and (s//3 >= a and s//3 >= b):
        print("YES")
    else:
        print("NO")