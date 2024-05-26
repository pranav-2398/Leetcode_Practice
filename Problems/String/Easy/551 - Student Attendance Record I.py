class Solution:
    def checkRecord(self, s: str) -> bool:
        count_a = 0
        count_l = 0
        res = 0
        for i in range(len(s)):
            if s[i] == 'A':
                count_a += 1
            elif s[i] == 'L':
                if i > 0 and s[i] == s[i - 1]:
                    count_l += 1
                else:
                    count_l = 1
            res = max(res, count_l)
        
        return True if count_a < 2 and res < 3 else False 