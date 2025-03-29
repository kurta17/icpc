def sum_ind(ind):
    return (1+ind) * ind//2

def dic_sum(ind):
    return ind/2 * (2*(n-1)+(1-ind))


for _ in range(int(input())):
    n,x = map(int, input().split())
    # 1, 2, 3, ... ,n 
    # sn = (1+n) * n/2
    if n == 1:
        print(1)
    elif x <= (1 + n) * n // 2:
        i = 1
        j = n
        while i < j:
            mid = (i + j) // 2
            if sum_ind(mid) < x:
                i = mid + 1
            else:
                j = mid
        print(i,'frec') 
    else:
        x-= (n*(n+1)//2)

        i = 1
        j = n-1
        while i < j:
            mid = (i + j) // 2
            if dic_sum(mid) < x:
                i = mid + 1
            else:
                j = mid
        print(i+n,'fvcrevf')