class Solution:
    def firstUniqChar(self, s: str) -> int:
        cache = {}
        for char in s:
            cache[char] = cache.get(char, 0) + 1
        
        for i in range(len(s)):
            if cache.get(s[i], 0) == 1:
                return i
        
        return -1