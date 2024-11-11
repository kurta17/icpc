t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    if n == 2:
        print(s[-1]-s[-2])
    else:
        every_s = sum(s[:-2])
        dak = s[-2] - every_s
        print(s[-1] - dak)