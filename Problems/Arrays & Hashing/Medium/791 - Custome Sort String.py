from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        counts = Counter(s)
        for char in order:
            res.append(char * counts.get(char, 0))
            if char in counts:
                del counts[char]
        
        if counts:
            for k, v in counts.items():
                res.append(k * v)
        
        return "".join(res)