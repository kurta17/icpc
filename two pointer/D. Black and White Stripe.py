t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    colors = input()
    l = 0
    
    count = {"B":0, "W":0}
    
    ans = float('inf')
    curr = 0

    for r in range(n):
        count[colors[r]] += 1

        if r-l+1 == k:    
            curr = count["W"]
            ans = min(curr,ans)
            count[colors[l]] -= 1
            l += 1
            

    print(ans)
