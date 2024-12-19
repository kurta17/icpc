t = int(input())

for _ in range(t):
    num = int(input())
    mtel = num // 33
    if mtel * 33 == num:
        print("YES")
    else:
        print("NO")
