t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    answer = -1

    for i in range(512):
        b = []
        for j in range(n):
            b.append(nums[j] ^ i)

        xor = b[0]

        for j in range(1,n):
            xor ^= b[j]

        if xor == 0:
            answer = i
            break

    if answer == -1:
        print(-1)
    else:
        print(answer)


        