from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarrsum = []
        MOD = 10 ** 9 + 7
        for i in range(n):
            cursum = 0
            for j in range(i, n):
                cursum = (cursum + nums[j]) % MOD
                subarrsum.append(cursum)

        subarrsum.sort()
        res = 0
        for i in range(left - 1, right):
            res = (res + subarrsum[i]) % MOD
        
        return res