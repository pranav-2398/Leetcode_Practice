class Solution:
    def minimumDeletions(self, s: str) -> int:
        acountright = [0] * len(s)
        for i in range(len(s) - 2, -1, -1):
            acountright[i] = acountright[i + 1]
            acountright[i] += 1 if s[i + 1] == 'a' else 0
        
        bcountleft = 0
        res = len(s)
        for i, c in enumerate(s):
            res = min(res, bcountleft + acountright[i])
            if c == 'b':
                bcountleft += 1
        
        return res