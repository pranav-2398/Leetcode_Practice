from math import log, floor

# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n < 0:
#             return False

#         limit = floor(log(n, 3))

#         for i in range(1, limit + 1):
#             if n ** (1/i) == 3:
#                 return True
#         return False

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            if n % 3 != 0:
                return False
            n = n // 3
        
        return n == 1

    
s = Solution()
print(s.isPowerOfThree(45))