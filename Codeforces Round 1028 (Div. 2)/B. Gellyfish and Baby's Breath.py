for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    pow2 = [pow(2, i, 998244353) for i in range(n)]

    ans = []

    p_max_val = -1
    p_max_ind = -1
    q_max_val = -1
    q_max_ind = -1

    
    for i in range(n):

        if p[i] > p_max_val:
            p_max_val = p[i]
            p_max_ind = i

        if q[i] > q_max_val:
            q_max_val = q[i]
            q_max_ind = i

        if p_max_val > q_max_val:
            ans.append((pow2[p_max_val] + pow2[q[i - p_max_ind]]) % 998244353)
        elif p_max_val == q_max_val:
            if q[i - p_max_ind] > p[i - q_max_ind]:
                ans.append((pow2[p_max_val] + pow2[q[i - p_max_ind]]) % 998244353)
            else:
                ans.append((pow2[p_max_val] + pow2[p[i - q_max_ind]]) % 998244353)
        else:
            ans.append((pow2[q_max_val] + pow2[p[i - q_max_ind]]) % 998244353)

    print(*ans)
    