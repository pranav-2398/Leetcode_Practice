class Solution:
    def getLucky(self, s: str, k: int) -> int:
        char = ''
        for c in s:
            char += str(abs(ord(c)- ord('a')) + 1)
        
        for i in range(k):
            val = 0
            for c in char:
                val += int(c)
            char = str(val)
        
        return val