from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxsum = nums[0]
        tempsum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                tempsum += nums[i]
                maxsum = max(maxsum, tempsum) 
            else:
                tempsum = nums[i]
                
        return maxsum  