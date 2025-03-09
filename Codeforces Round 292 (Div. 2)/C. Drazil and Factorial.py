n = int(input())
a = list(map(int,input().strip()))
ans = []

for i in a:
    if i in [2,3,5,7]:
        ans.append(i)
    elif i == 4:
        ans.append(3)
        ans.append(2)
        ans.append(2)
    elif i == 6:
        ans.append(5)
        ans.append(3)
    elif i == 8:
        ans.append(7)
        ans.append(2)
        ans.append(2)
        ans.append(2)
    elif i == 9:
        ans.append(7)
        ans.append(3)
        ans.append(3)
        ans.append(2)

ans.sort(reverse = True)
print(''.join(map(str,ans))) 



    