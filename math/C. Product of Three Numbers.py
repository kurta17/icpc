t = int(input())

for _ in range(t):
    n = int(input())
    k = n
    a = 1
    b = 1
    for i in range(2, int(k**0.5)+1):
        if k % i == 0:
            k //= i
            a = i
            break
    for i in range(a+1, int(k**0.5)+1):
        if k % i == 0:
            k //= i
            b = i
            break

    if a != 1 and b != 1 and k != 1 and k != a and k != b and a*b*k == n:
        print("YES")
        print(a, b, k)
    else:
        print("NO")