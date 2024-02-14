from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
        
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        
        nums = sorted(nums, key = cmp_to_key(compare))

        return str(int("".join(nums)))

s = Solution()
nums = [111311, 1113]
# nums = [3,30,34,5,9]
print(s.largestNumber(nums))
