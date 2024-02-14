########## MY SOLN ##########################

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         cache = {}

#         def helper(n):
#             sum = 0
#             while n:
#                 sum += (n % 10) ** 2
#                 n = n // 10
#             return sum

#         sum = 0
#         while sum != 1:
#             sum = helper(n)
#             if sum in cache:
#                 return False
#             else:
#                 cache[sum] = 1
#             n = sum

#         return True

##################################################


##### ANOTHER SOLN ###############################

class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
            
        return False
    
    def sumOfSquares(self, n: int) -> int:
        res = 0

        while n:
            res += (n % 10) ** 2
            n = n // 10
        
        return res
    
###################################################

s = Solution()
print(s.isHappy(2))