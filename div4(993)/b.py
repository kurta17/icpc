t = int(input())

for _ in range(t):
    a = list(map(str, input().strip()))
    ans = []
    for i in range(len(a)-1,-1,-1):
        if a[i] == "q":
            ans.append("p")
        elif a[i] == "p":
            ans.append("q")
        else:
            ans.append("w")
    print(''.join(ans))