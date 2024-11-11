import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    prefix_sum = 0
    seen_sum = {0:-1}
    ans = 0
    last_pos = -1
    for i in range(n):
        prefix_sum += a[i]

        if prefix_sum in seen_sum and seen_sum[prefix_sum] >= last_pos:
            ans += 1
            last_pos = i+1
            seen_sum = {0: i + 1}
        else:
            seen_sum[prefix_sum] = i+1
        print(seen_sum)
    print(ans)
