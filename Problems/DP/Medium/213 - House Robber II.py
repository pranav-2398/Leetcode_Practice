from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1 = rob2 = 0

        for i in range(len(nums) - 1, -1, -1):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp 
        
        return rob2