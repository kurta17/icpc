t = int(input())
pe = 0

for _ in range(t):
    a,n = (map(str, input().split()))

    if a == "P":
        pe += int(n)
    else:
        can_ent = int(n)
        if can_ent > pe:
            print("YES")
            pe = 0
        else:
            print("NO")
            pe = pe - can_ent
