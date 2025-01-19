t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    even_max = 0
    number_ev = 0
    odd_max = 0
    number_od = 0
    for i in range(n):
        if i % 2 == 0:
            number_ev += 1    
            even_max = max(even_max, a[i])
        else:
            number_od += 1    
            odd_max = max(odd_max, a[i])

    ans_ev = even_max + number_ev
    ans_od = odd_max + number_od

    if n > 0:
        print(max(ans_ev, ans_od))
    else:
        print(0)