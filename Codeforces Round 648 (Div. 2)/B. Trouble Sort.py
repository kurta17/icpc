from collections import defaultdict


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    zero = []
    one = []

    for i in range(n):
        if b[i] == 0:
            zero.append(a[i])
        else:
            one.append(a[i])
    if sorted(one) == one and sorted(zero) == zero or (len(one) > 0 and len(zero) > 0):
        print("YES")
    else:
        print("NO")


