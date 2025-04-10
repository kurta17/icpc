def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

for _ in range(int(input())):
    x,k = (map(int,input().split()))
    
    if k == 1 and is_prime(x):
        print("YES")
    elif x == 1 and k == 2:
        print("YES")
    else:
        print("NO")