from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3 : return - 1
        nums.sort()
        presum = []
        start = 0
        for num in nums:
            presum.append(start + num)
            start = presum[-1]
        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < presum[i - 1]:
                return presum[i]
                
        return -1
    
s = Solution()
nums = [5,5,5]
# nums = [1,12,1,2,5,50,3]
print(s.largestPerimeter(nums))