s = str(input())
ab = False
ba = False
found = False
last = -1
for i in range(1,len(s)):
    if s[i-1:i+1] == "AB" and last != i-1 and ab==False:
        last = i
        ab = True
        found = True
    if s[i-1:i+1] == "BA" and last != i-1 and ba==False and found == True:
        last = i
        ba = True

ab1 = False
ba1 = False
found1 = False
lst = -1
for i in range(1,len(s)):
    if s[i-1:i+1] == "BA" and lst != i-1 and ba1==False:
        lst = i
        ba1 = True
        found1 = True
    if s[i-1:i+1] == "AB" and lst != i-1 and ab1==False and found1 == True:
        lst = i
        ab1 = True
    

if (ab and ba) or (ab1 and ba1):
    print("YES")
else:
    print("NO")

