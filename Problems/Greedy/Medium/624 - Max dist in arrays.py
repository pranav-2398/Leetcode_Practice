from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minele = arrays[0][0]
        maxele = arrays[0][-1]
        res = 0
        for i in range(1, len(arrays)):
            res = max(
                res,
                max(arrays[i][-1] - minele, maxele - arrays[i][0])
            )
            minele = min(minele, arrays[i][0])
            maxele = max(maxele, arrays[i][-1])
        
        return res