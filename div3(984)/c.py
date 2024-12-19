t=int(input())
for _ in range(t):
    a = list(map(str,input().strip()))
    n = int(input())
    count = 0
    for i in range(len(a)-3):
        if a[i:i+4] == ['1','1','0','0']:
            count += 1

    for _ in range(n):
        i,v = map(int,input().split())
        i -= 1
        curr = ''.join(a[max(0,i-3):i+4]).count("1100")
        a[i] = str(v)
        now =  ''.join(a[max(0,i-3):i+4]).count("1100")
        count += now - curr
        print("YES" if count>0 else "NO")
