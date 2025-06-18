for _ in range(int(input())):
    n = int(input())
    d = list(map(int, input().split()))
    minxmax = []

    for _ in range(n):
        l, r = map(int, input().split())
        minxmax.append((l, r))

    val_range = [(0,0)] * (n + 1)
    poss = True

    for i in range(1,n+1):
        l_i, r_i = minxmax[i - 1]
        prev_L, prev_R = val_range[i - 1]
        d_val = d[i - 1]

        min_h_inc = 0 if d_val != 1 else 1
        max_h_inc = 1 if d_val != 0 else 0

        pot_l = prev_L + min_h_inc
        pot_r = prev_R + max_h_inc

        L_i = max(pot_l, l_i)
        R_i = min(pot_r, r_i)

        if L_i > R_i:
            poss = False
            break

        val_range[i] = (L_i, R_i)

    if not poss:
        print(-1)
    else:
        ans = [0] * n
        h = val_range[n][0]
        for i in range(n,0,-1):
            L_prev, R_prev = val_range[i - 1]
            d_val = d[i - 1]

            min_h_inc = 0 if d_val != 1 else 1
            max_h_inc = 1 if d_val != 0 else 0

            targ_pre_l = max(L_prev, h - max_h_inc)
            h_prev = targ_pre_l
            ans[i - 1] = h - h_prev
            h = h_prev

        print(*ans)
