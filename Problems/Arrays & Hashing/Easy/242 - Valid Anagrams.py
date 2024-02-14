class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        x = list(s)
        x.sort()
        y = list(t)
        y.sort()

        for i in range(min(len(x), len(y))):
            if x[i] != y[i]:
                return False
        
        return True
        