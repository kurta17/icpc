import math
for _ in range(int(input())):
    n = int(input())
    if n % 2 == 1 and n != 1 or n == 2:
        print("Ashishgup")
    elif n == 1:
        print("FastestFinger")
    else:
        ashi = False
        for i in range(3, int(n ** 0.5) + 1):
            if n % i == 0:
                if i % 2 == 1 or (n // i) % 2 == 1:
                    ashi = True
                    break
        if ashi:
            print("Ashishgup")
        else:
            print("FastestFinger")
    
            
        
                