from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_count = {0 : 1}
        prefixsum = 0
        res = 0

        for n in nums:
            prefixsum += n
            rem = prefixsum % k

            res += rem_count.get(rem, 0)
            rem_count[rem] = 1 + rem_count.get(rem, 0)
        
        return res