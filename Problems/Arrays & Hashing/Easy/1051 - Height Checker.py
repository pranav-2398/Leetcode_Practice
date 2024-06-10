from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sorted = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != heights_sorted[i]:
                res += 1
        return res