limit = 10 ** 4 + 1
sieve = [True] * (limit + 1)
sieve[0] = sieve[1] = False
for i in range(2, int(limit ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * i, limit + 1, i):
            sieve[j] = False
primes = [i for i, is_prime in enumerate(sieve) if is_prime]
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    
    cum_sum = 0
    max_k = 0
    curr_ind = 0
    
    for i in range(n):
        p = primes[curr_ind]
        if p <= a[i]:
            cum_sum += a[i] - p
        else:
            cum_sum += -(p - a[i])
        if cum_sum >= 0:
            max_k = i + 1
        curr_ind += 1
    
    print(n - max_k)