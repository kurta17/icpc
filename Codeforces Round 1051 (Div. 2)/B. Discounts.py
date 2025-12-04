for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort(reverse=True)
    b.sort()
    bpref = [b[0]-1]
    for o in range(1,k):
        bpref.append(bpref[-1] + b[o])
    
    # print(a)
    # print(bpref)
    i = 0
    ans = 0
    j = 0
    while i < n and j < k:
        if i != bpref[j]:
            ans += a[i]
        else:
            j+=1
            if (j < k and b[j] > n-i) or j >= k:
                ans += sum(a[i+1:])
                break
        i+=1

    print(ans)
    