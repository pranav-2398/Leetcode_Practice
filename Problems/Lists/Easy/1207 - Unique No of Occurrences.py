from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        freq_count = Counter(freq.values())
        
        if sum(freq_count.values()) > len(freq_count.keys()):
            return False
        else:
            return True