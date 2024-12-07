# import bisect
# t=  int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int,input().split()))

#     dp = [0 for _ in range(n)]
#     for i in range(1,n):
#         if a[i] != a[i-1]:
#             dp[i] = dp[i-1] +1 
#         else:
#             dp[i] = dp[i-1]

#     q = int(input())
#     for _ in range(q):
#         l,r = map(int,input().split())
#         if dp[r-1] - dp[l-1] == 0:
#             print(-1,-1)
#         else:
#             ind = bisect.bisect_right(dp,dp[l-1])
#             print(l,ind+1)

