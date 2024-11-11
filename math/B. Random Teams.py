n, m = map(int, input().split())

if n == 1:
    print(0, 0)
else:
    k = n - m + 1
    kmax = k * (k - 1) // 2
    
    
    person_per = n //  m
    extra = n % m
    full = m - extra
    ex_team = extra

    kmin = (full * (person_per - 1) * person_per // 2) + (extra * (person_per + 1) * person_per // 2)
    print(kmin, kmax)
    

