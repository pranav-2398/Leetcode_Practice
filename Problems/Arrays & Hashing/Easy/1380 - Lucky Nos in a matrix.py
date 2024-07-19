from collections import defaultdict
from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        row_map = defaultdict(lambda: float("inf"))
        col_map = defaultdict(int)

        for i in range(row):
            for j in range(col):
                row_map[i] = min(row_map[i], matrix[i][j])
                col_map[j] = max(col_map[j], matrix[i][j])

        return list(set(row_map.values()) & set(col_map.values()))