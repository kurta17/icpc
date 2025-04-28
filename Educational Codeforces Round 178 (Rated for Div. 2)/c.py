from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    a = list(map(str, input().strip()))

    d = defaultdict(int)
    for i in a:
        d[i] += 1

    if a[-1] == "B" and d["B"] == 1:
        print("Alice")
    elif a[-1] == "B" and d["B"] > 1:
        print("Bob")
    elif a[-1] == "A" and d["A"] == 1:
        print("Bob")
    elif a[0] == "B" and a[-2] == "B":
        print("Bob")
    else:
        print("Alice")

