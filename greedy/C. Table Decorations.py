colors = list(map(int, input().split()))

s = sum(colors)
minval = min(colors)
maxval = max(colors)

if maxval >= 2 * (s- maxval):
    print(s - maxval)
else:
    print(s//3)