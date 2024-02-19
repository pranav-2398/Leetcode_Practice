### MY SOLN ##################################
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 2 or not n:
            return False
        else:
            return self.isPowerOfTwo(n // 2)
##############################################

s = Solution()
print(s.isPowerOfTwo(16))