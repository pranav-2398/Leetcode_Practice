from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapdict = {i:n for i, n in enumerate(mapping)}
        res = []
        i = 0
        for num in nums:
            val = ''
            for s in str(num):
                val += str(mapdict[int(s)])
            res.append((int(val), i))
            i += 1
       
        res.sort()

        return [nums[i] for (val, i) in res]