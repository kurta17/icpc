import math


n,k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))

def find_el(arr, x):
    if x > arr[-1]:
        return len(arr)+1
    
    l, r = 0, len(arr)-1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l+1
for i in q:
    print(find_el(a, i))
        
