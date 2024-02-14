class Solution:
    ### WITHOUT MEMOIZATION #####################################
    # def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    #     MOD = 10**9 + 7

    #     def count(n, target):
    #         if n == 0:
    #             return 1 if target == 0 else 0
            
    #         res = 0
    #         for i in range(1, k+1):
    #             res = (res + count(n-1, target-i)) % MOD
            
    #         return res
        
    #     return count(n, target)
    
    ################################################################

    ####### MEMOIZATION ############################################

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        memo = {}

        def count(n, target):
            if n == 0:
                return 1 if target == 0 else 0
            
            if (n, target) in memo:
                return memo[(n, target)]
            
            res = 0
            for i in range(1, k+1):
                res = (res + count(n-1, target-i)) % MOD
            
            memo[(n, target)] = res

            return res
        
        return count(n, target)
    
    #######################################################################

s = Solution()
print(s.numRollsToTarget(2,6,7))
