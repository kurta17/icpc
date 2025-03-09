for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print(n//2,n//2)
    else:
        a = 1
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                a = i
                break
            
        if a == 1:
            print(1,n-1)
        else:
            print(n//a,n-n//a)

