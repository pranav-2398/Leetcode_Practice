from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return -1 
            
        store = {}

        for i in range(len(nums)):
            if nums[i] in store:
                return [store[nums[i]], i]
            else:
                complement = target - nums[i]
                store[complement] = i

soln = Solution()
print(soln.twoSum([3,3], 6))