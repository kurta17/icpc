from bisect import bisect_left

for _ in range(int(input())):
    n, m = map(int, input().split())
    tot = []
    
    for _ in range(n):
        a = list(map(int, input().split()))
        pref = [a[0]]
        for i in range(1, m):
            pref.append(pref[-1] + a[i])
        tot.append((sum(a), pref)) 
    tot.sort(reverse=True, key=lambda x: x[0])
    
    final_array = []
    for _, row in tot:
        final_array.extend(row)
    
    total_score = 0
    prefix_sum = 0
    for num in final_array:
        prefix_sum += num
        total_score += prefix_sum
    
    print(total_score)
