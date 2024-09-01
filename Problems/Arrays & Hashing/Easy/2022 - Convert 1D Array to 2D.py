from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        
        new = [ [] for i in range(m)]

        for i in range(len(original)):
            new[i // n].append(original[i])
        
        return new