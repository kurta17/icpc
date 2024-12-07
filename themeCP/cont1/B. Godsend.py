n = int(input())
nums = list(map(int, input().split()))

odd = 0
even = 0
s = 0

for i in nums:
    s += i
    if i % 2 == 0:
        even+=1
    else:
        odd+=1

if s % 2 == 1:
    print("First")
elif odd == 0:
    print("Second")
elif odd % 2 == 0:
    print("First")
