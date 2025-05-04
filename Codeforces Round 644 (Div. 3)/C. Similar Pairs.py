# from bisect import bisect_left
# import math
# math.ceil

# def found(arr, val):
#     pos = bisect_left(arr, val - 1)
#     if pos < len(arr) and arr[pos] == val - 1:
#         return True
#     pos = bisect_left(arr, val + 1)
#     if pos < len(arr) and arr[pos] == val + 1:
#         return True
#     return False

# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     e = sum(1 for x in a if x % 2 == 0)
#     o = n - e 
#     if e % 2 != o % 2:
#         print("NO")
#     elif e % 2 == 0:
#         print("YES")
#     else:
#         eve = sorted(x for x in a if x % 2 == 0)
#         odd = sorted(x for x in a if x % 2 == 1)
#         for val in eve:
#             if found(odd, val):
#                 print("YES")
#                 break
#         else:
#             print("NO")



import math
for _ in range(int(input())):
    n,k = (map(int, input().split()))
    if k == 1:
        print(1)
    elif n > k:
        if n % k == 0:
            print(1)
        else:
            print(2)
    else:
        print(math.ceil(k/n))
