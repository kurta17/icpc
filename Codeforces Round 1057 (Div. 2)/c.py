from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = Counter(a)

    pairsum = 0
    pairc = 0
    darch = []

    for i, cnt in d.items():
        pair = cnt // 2
        if pair:
            pairc += pair
            pairsum += 2 * i * pair
        if cnt % 2:
            darch.append(i)

    if pairsum == 0:
        print(0)
        continue

    ans = pairsum

    if darch:
        if len(darch) > 1:
            darch.sort(reverse=True)
            if darch[0] < pairsum:
                ans = pairsum + darch[0]
            for i in range(1, len(darch)):
                diff = darch[i - 1] - darch[i]
                if diff < pairsum:
                    ans = max(ans, pairsum + darch[i - 1] + darch[i])
                if darch[i] < pairsum:
                    ans = max(ans, pairsum + darch[i])
        else:
            if darch[0] < pairsum:
                ans = pairsum + darch[0]

    if ans == pairsum and pairc == 1:
        print(0)
    else:
        print(ans)
