def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    total_sum = sum(a)
    a.sort()
    max_card = a[-1]
    need = sum(max_card - x for x in a)

    if k >= need:
        print(n)
    else:
        answer = 1
        for i in range(2, n + 1):
            x = i - (total_sum % i)
            y = i * max_card - total_sum

            if x < y:
                z = (y - x + i - 1) // i
                x += z * i
            elif x > y:
                z = (x - max(0, y)) // i
                x -= z * i

            if k >= x:
                answer = max(answer, i)
        
        print(answer)

t = int(input())
for _ in range(t):
    solve()
