n = int(input())
a = list(map(int, input().split()))
q = int(input())
a.sort()

def count_left(arr, left):
    l,r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < left:
            l = mid + 1
        else:
            r = mid
    return l

def count_right(arr, left):
    l,r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] <= left:
            l = mid + 1
        else:
            r = mid
    return l
print(a)        
for _ in range(q):
    left,right = map(int, input().split())
    print(count_right(a,right), count_left(a,left))

