from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0
        for word in words:
            valid = True
            for c in word:
                if c not in allowed:
                    valid = False
                    break
            if valid:
                res += 1
        
        return res