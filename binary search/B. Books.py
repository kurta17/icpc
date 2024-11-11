n,t = map(int, input().split())
books = list(map(int, input().split()))


i = 0
j = 0
sum = 0
max = 0

while j < n:
    sum += books[j]
    if sum <= t:
        if j-i+1 > max:
            max = j-i+1
    else:
        while sum > t:
            sum -= books[i]
            i += 1
    j += 1
    
print(max)
