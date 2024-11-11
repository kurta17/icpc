for i in range(10**3,2500):
    if len(str(i * 4)) == 4 and str(i * 4)[1:3] == str(i)[0:2]:
        print(i)
        
