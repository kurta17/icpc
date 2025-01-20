n = int(input())
a = list(map(int, input().split()))

c4,c8,c15,c16,c23,c42 = 0,0,0,0,0,0

for i in a:
    if i == 4:
        c4 += 1
    elif i == 8 and c4 > 0:
        c8 += 1
        c4 -= 1
    elif i == 15 and c8 > 0:
        c15 += 1
        c8 -= 1
    elif i == 16 and c15 > 0:
        c16 += 1
        c15 -= 1
    elif i == 23 and c16 > 0:
        c23 += 1
        c16 -= 1
    elif i == 42 and c23 > 0:
        c42 += 1
        c23 -= 1

print(n - c42 * 6)
    