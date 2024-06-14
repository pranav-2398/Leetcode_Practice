from collections import defaultdict
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        count = defaultdict(int)
        count[nums[0]] = 1
        for i in range(1, len(nums)):
            if count[nums[i]]:
                change = abs(nums[i] - nums[i-1]) + 1
                res += change
                nums[i] += change
            count[nums[i]] += 1
    
        return res

s = Solution()
nums = [3,2,1,2,1,7]
print(s.minIncrementForUnique(nums))