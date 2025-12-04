def digit_sum_upto(n):
    if n <= 0:
        return 0
    ans = 0
    length = len(str(n))
    p10 = 10**(length-1)
    while p10 > 0:
        msd = n // p10
        rest = n % p10
        ans += msd * 45 * (p10//10) * (length-1)
        ans += (msd*(msd-1)//2) * p10
        ans += msd * (rest + 1)
        n = rest
        p10 //= 10
        length -= 1
    return ans

blocks = [0]
for d in range(1, 17):
    blocks.append(blocks[-1] + d * 9 * (10 ** (d - 1)))

for _ in range(int(input())):
    k = int(input())
    last_b = 0
    for i in range(len(blocks)):
        if k < blocks[i]:
            last_b = i - 1
            break

    last_dig_bl = 10**last_b - 1
    sum_bl = digit_sum_upto(last_dig_bl)
    darch = k - blocks[last_b]

    nash = darch % (last_b+1)
    wholedig = darch // (last_b+1)
    sum_darch = 0
    lastwholedig = 0
    sum_nasht = 0
    if wholedig != 0:
        lastwholedig = last_dig_bl + wholedig
        sum_darch = digit_sum_upto(lastwholedig) - digit_sum_upto(last_dig_bl)
    if nash != 0:
        lastpartdig = str(lastwholedig + 1)
        for i in lastpartdig[:nash]:
            sum_nasht += int(i)

    print(sum_bl + sum_darch + sum_nasht)
