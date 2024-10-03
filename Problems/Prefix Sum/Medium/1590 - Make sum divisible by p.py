from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remain = total % p

        if not remain:
            return 0
        
        res = len(nums)
        cursum = 0
        remidx= {
            0: -1
        }

        for i, n in enumerate(nums):
            cursum = (cursum + n) % p
            prefix = (cursum - remain + p) % p
            if prefix in remidx:
                length = i - remidx[prefix]
                res = min(res, length)
            remidx[cursum] = i
        
        return -1 if res == len(nums) else res