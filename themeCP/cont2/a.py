t = int(input())

for _ in range(t):
    n = int(input())
    cord = list(map(str, input().strip()))
    emp = [1 if cord[0] == "." else 0]

    for i in range(1,n):
        if cord[i] == cord[i-1] and cord[i] == ".":
            emp[-1] += 1
        elif cord[i] != cord[i-1] and cord[i] == ".":
            emp.append(1)
        else:
            emp.append(0)
    ans = 0
    for i in emp:
        if i == 1:
            ans += 1
        elif i == 2:
            ans += 2
        elif i > 2:
            ans = 2
            break
            
    print(ans)
