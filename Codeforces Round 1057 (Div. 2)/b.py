for _ in range(int(input())):
    x,y,z = map((int), input().split())
    if x&y == y&z == z&x:
       print("YES")
    else:
       print("NO")