from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        r = len(nums)
        while i < r:
            print(nums)
            print(nums[i])
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                r-=1
            else:
                i+=1
                r-=1
            


s = Solution()
nums = [0,1,0,3,12]
s.moveZeroes(nums)