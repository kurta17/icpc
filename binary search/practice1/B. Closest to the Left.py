import math


n,k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))

def find_el(arr, x):
    l, r = 0, len(arr)
    while r-l > 1:
        mid = int(math.floor((l + r) / 2))
        if arr[mid] <= x:
            l = mid
        else:
            r = mid
    return 0 if arr[0] > x else l+1

for i in q:
    print(find_el(a, i))
        
