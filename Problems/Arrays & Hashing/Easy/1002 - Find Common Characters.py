from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])

        for i in range(1, len(words)):
            count_temp = Counter(words[i])
            for key in count.keys():
                count[key] = min(count[key], count_temp[key])

        res = []
        for key, val in count.items():
            for _ in range(val):
                res.append(key)

        return res