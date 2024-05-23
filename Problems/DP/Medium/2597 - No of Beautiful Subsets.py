from collections import defaultdict
from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        def helper(i, count):
            if  i == len(nums):
                return 1
            
            res = helper(i + 1, count)
            if not count[nums[i] + k] and not count[nums[i] - k]:
                count[nums[i]] += 1
                res += helper(i + 1, count)
                count[nums[i]] -= 1
            
            return res
        
        return helper(0, defaultdict(int))
    
s = Solution()
# nums = [2, 4, 6]
nums = [10,4,5,7,2,1]
print(s.beautifulSubsets(nums, 3))