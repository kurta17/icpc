for _ in range(int(input())):
    a,b = map(int,input().split())
    print("Bob") if (a+b)%2 == 0 else print("Alice")