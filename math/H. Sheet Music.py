MOD = 998244353

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def count_songs(n, k):
    # Step 1: Compute the number of relationship sequences
    rel_seqs = mod_exp(3, n-1, MOD)
    
    # Step 2: Compute the total number of valid assignments
    valid_assignments = mod_exp(k, n, MOD)
    
    # Step 3: Combine results
    return (rel_seqs * valid_assignments) % MOD

# Input
n, k = map(int, input().split())

# Output
print(count_songs(n, k))
