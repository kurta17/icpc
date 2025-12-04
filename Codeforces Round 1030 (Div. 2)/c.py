coins = [(1,3)]
for i in range(1,40):
    coins.append((3**i, 3**(i+1) + i * 3**(i-1)))

for _ in range(int(input())):
    n = int(input())
    ans = 0
    while n > 0:
        for i in range(len(coins)):
            if n < coins[i][0]:
                n -= coins[i-1][0]
                ans += coins[i-1][1]
                break
    print(ans)

