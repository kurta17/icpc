bets = list(map(int, input().split()))
total = sum(bets)
n = len(bets)

if total % n == 0 and total != 0:
    print(total // n)
else:
    print(-1)