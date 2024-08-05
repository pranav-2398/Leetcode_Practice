from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        countk = Counter(arr)
        for key in countk:
            if countk[key] == 1:
                k -= 1
            if not k:
                return key
        return ""