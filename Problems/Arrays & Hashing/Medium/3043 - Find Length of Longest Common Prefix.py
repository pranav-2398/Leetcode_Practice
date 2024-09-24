from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        prefixset = set()
        for n in arr1:
            while n and n not in prefixset:
                prefixset.add(n)
                n = n // 10
        
        res = 0
        for n in arr2:
            while n and n not in prefixset:
                n = n // 10
            if n:
                res = max(res, len(str(n)))
        return res