t = int(input())

for _ in range(t):
    n = (input())
    ss = 0
    ori = 0
    sami = 0
    ans = False

    for i in n:
        i = int(i)
        if i == 2:
            ori += 1
        if i == 3:
            sami += 1
        ss += i
        
    if ss % 9 == 0:
        print("YES")
    else:
        a,b = min(sami,9),min(ori,9)
        for j in range(b+1):
            for i in range(a+1):
                if (6*i + 2*j + ss) % 9 == 0:
                    ans = True
                    

        if not ans:
            print("NO")
        else:
            print("YES")
        


        

    

