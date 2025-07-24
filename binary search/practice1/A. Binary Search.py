import math


n,k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))

def find_el(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = int(math.floor((l + r) / 2))
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            l = mid+1
        else:
            r = mid-1
    return False

for i in q:
    if find_el(a, i):
        print("YES")
    else:
        print("NO")
