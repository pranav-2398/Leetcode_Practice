from collections import defaultdict
from typing import List

### Sliding Window with 3 Pointers ###################################
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        res = 0
        l_far = 0
        l_near = 0
        
        for r in range(len(nums)):
            count[nums[r]] += 1

            while len(count) > k:
                count[nums[l_near]] -= 1
                if count[nums[l_near]] == 0:
                    count.pop(nums[l_near])
                l_near += 1
                l_far = l_near

            while count[nums[l_near]] > 1:
                count[nums[l_near]] -= 1
                l_near += 1

            if len(count) == k:
                res += l_near - l_far + 1
            
        return res

######################################################################
s = Solution()
# nums = [1,2,1,2,3]
# k = 2
# nums = [1, 2, 1, 3, 4]
# k = 3
nums = [1, 2, 2, 1, 3, 2, 2, 4]
k = 3
print(s.subarraysWithKDistinct(nums, k))
        
        