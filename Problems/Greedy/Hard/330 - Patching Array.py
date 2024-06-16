from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i, output, upto = 0, 0, 0
        N = len(nums)
        while upto < n:
            if i < N and nums[i] <= upto + 1:
                upto += nums[i]
                i += 1
            else:
                output += 1
                upto += upto + 1
        return output
    
s = Solution()
nums = [1, 3]
n = 6
print(s.minPatches(nums, n))