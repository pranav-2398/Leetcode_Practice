from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = {}
        res = []

        for n in nums:
            row = count.get(n, 0)
            if len(res) == row:
                res.append([])

            count[n] = 1 + count.get(n,0)
            res[row].append(n)

        return res