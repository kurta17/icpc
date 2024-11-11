# t = int(input())

# for _ in range(t):
#     n,k = map(int,input().split())
#     col = list(input().strip())
   
#     i = 0
    
#     cnt = 0

#     while i + k < n:
#         if col[i] == "W":
#             i += 1
            
#         elif col[i] == "B":
#             i += k
#             cnt += 1

            
#     if "B" in col[i:]:
#         cnt += 1
#     print(cnt)

# d = {"av": 1, "bb": 2}

# print(d["av"])

import collections
from typing import List

from collections import defaultdict
class Solution:
    def compress(self, chars: List[str]) -> int:
        d = defaultdict(int)
        for i in chars:
            d[i] += 1
        print(d['a'])


s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))


