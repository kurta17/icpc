s = list(map(str, input().strip()))
op = False
sq = []
i = 0
j = len(s)-1
while i < j:
    if '(' == s[i]:
        while i < j:
            if ')' == s[j]:
                sq.append(i+1)
                sq.append(j+1)
                break
            else:
                j-=1
        j-=1
        i+=1
    else:
        i+=1
if len(sq) == 0:
    print(0)
else:
    print(1)
    print(len(sq)) 
    sq.sort()
    print(*(sq))