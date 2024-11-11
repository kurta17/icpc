t = int(input())

for _ in range(t):
    numbers = input()
    n = len(numbers)
    l = 0
    
    count = {"1":0, "2":0, "3":0}
    count[numbers[0]] += 1
    

    size = float('inf')
    curr = 0
    

    for r in range(1,n):
        count[numbers[r]] += 1
        
        if count["1"] != 0 and count["2"] != 0 and count["3"] != 0:
            while count["1"] != 0 and count["2"] != 0 and count["3"] != 0:
                l += 1
                count[numbers[l-1]] -= 1

            curr = r - l + 2
            size = min(size,curr)
           


    if size == float('inf'):
        print(0)
    else:
        print(size)

        


