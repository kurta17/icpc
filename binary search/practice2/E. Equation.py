c = float(input())

def f(x):
    return x ** 2 + x ** 0.5 >= c

l = 1
r = 1

while not f(r): r *= 2

for i in range(70):
    mid = (l+r) / 2
    if f(mid):
        r = mid
    else:
        l = mid

print(l)