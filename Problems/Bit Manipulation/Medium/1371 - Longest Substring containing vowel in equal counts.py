class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels= "aeiou"

        res = 0
        mask = 0
        masktoidx = {0:-1}

        for i, c in enumerate(s):
            if c in vowels:
                mask = mask ^ (1 + ord(c) - ord('a'))
            if mask in masktoidx:
                length = i - masktoidx[mask]
                res = max(res, length)
            else:
                masktoidx[mask] = i
        return res