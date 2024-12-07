t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    cord = list(map(int, input().split()))

    cord.sort()

    cat = 0
    last = n
    i = k - 1
    mice = 0

    while i >= 0 and cat < last:
        cat += n - cord[i]
        last = cord[i-1]
        mice += 1
        i -= 1
    print(mice)
