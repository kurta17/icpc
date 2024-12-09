t = int(input())

for _ in range(t):
    n = int(input())
    ans = 1
    j = 2
    
    while j < n+1:
        j = 2 * j + 1
        ans += 1
        
    
    print(ans)

 
