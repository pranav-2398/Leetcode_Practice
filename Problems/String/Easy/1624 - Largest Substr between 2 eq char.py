class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        cache = {}

        res = -1 
        for i in range(len(s)):
            if s[i] in cache:
                res = max(res,i - 1 - cache[s[i]])
            else:
                cache[s[i]] = i
        
        return res