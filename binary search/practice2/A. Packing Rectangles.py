def check(x, w, h, n):
    return (x // w) * (x // h) >= n

w, h, n = map(int, input().split())

l = 0
r = 1
while not check(r, w, h, n):
    r *= 2

while r > l + 1:
    mid = (l + r) // 2
    if check(mid, w, h, n):
        r = mid
    else:
        l = mid

print(r)