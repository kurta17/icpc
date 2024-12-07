t = int(input())

for _ in range(t):
    n = list(map(int, input().strip()))

    for i in range(len(n)):
        for j in range(i+1, min(i + 10, len(n))):
            if n[i] < n[j] - (j - i):
                n[j] = n[j] - (j - i)
                temp = n[j]
                for k in range(j, i, -1):
                    n[k] = n[k-1]
                n[i] = temp
        
    print(''.join(map(str,n)))