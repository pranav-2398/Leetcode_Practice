from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        sub_sum = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                top = sub_sum[r - 1][c] if r > 0 else 0
                left = sub_sum[r][c - 1] if c > 0 else 0
                top_left = sub_sum[r - 1][c - 1] if min(r, c) > 0 else 0
                sub_sum[r][c] = matrix[r][c] + top + left - top_left

        res = 0
        for r1 in range(rows):
            for r2 in range(r1, rows):
                count = defaultdict(int)
                count[0] = 1
                for c in range(cols):
                    cur_sum = sub_sum[r2][c] - (
                        sub_sum[r1 - 1][c] if r1 > 0 else 0
                    )
                    diff = cur_sum - target
                    res += count[diff]
                    count[cur_sum] += 1

        return res