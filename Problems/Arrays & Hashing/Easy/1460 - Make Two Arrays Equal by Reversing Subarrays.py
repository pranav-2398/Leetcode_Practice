from collections import Counter
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counttarget = Counter(target)
        countarr = Counter(arr)

        for k in counttarget:
            if k not in countarr or counttarget[k] != countarr[k]:
                return False
        
        return True