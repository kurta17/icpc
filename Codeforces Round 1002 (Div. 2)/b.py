for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    if n == m:
        k = 1
        for i in range(1, n, 2):
            if a[i] != k:
                break
            k += 1
        print(k)
    else:
        found_non_one = False
        for i in range(1, n - m + 2):
            if a[i] != 1:
                print(1)
                found_non_one = True
                break
        if not found_non_one:
            print(2)
