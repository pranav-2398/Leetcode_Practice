from typing import List
from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        res = []
        for n in arr2:
            for i in range(count[n]):
                res.append(n)
            del count[n]

        for n in sorted(count.keys()):
            for i in range(count[n]):
                res.append(n)
        return res