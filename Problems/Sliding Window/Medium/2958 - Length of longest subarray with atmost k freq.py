from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        count = defaultdict(int)

        for right in range(len(nums)):
            count[nums[right]] += 1

            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
    
s = Solution()
nums = [1,2,3,1,2,3,1,2]
k = 2
print(s.maxSubarrayLength(nums, k))
