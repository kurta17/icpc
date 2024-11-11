n = int(input())
dots = list(map(int,input().split()))
ans = 0

for i in range(2,n):
    m = min(dots[i],dots[i-1],dots[i-2])
    ans += m
    dots[i] -= m
    dots[i-1] -= m
    dots[i-2] -= m

print(ans)

# for i in range(1,n):
#     if dots[i] > 0 and dots[i-1] > 0:
#         if dots[i] > dots[i-1]:
#             if dots[i-1] * 2 < dots[i]:
#                 ans += dots[i-1] * 2
#                 dots[i] = dots[i] - dots[i-1] * 2
#                 dots[i-1] = 0
#             else:
#                 ans += dots[i]//2
#                 dots[i-1] -= dots[i] // 2
#                 dots[i] -= dots[i]
                
#         else:
#             if dots[i] * 2 < dots[i-1]:
#                 ans += dots[i] 
#                 dots[i-1] = dots[i-1] - dots[i] * 2
#                 dots[i] = 0
#             else:
#                 ans += dots[i-1]//2
#                 dots[i] -= dots[i-1]
#                 dots[i-1] -= dots[i-1]//2

# print(dots)
# print(ans)

