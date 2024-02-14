##### RECURSIVE SOLN ##########################################################
# class Solution:
#     def kInversePairs(self, n: int, k: int) -> int:
#         MOD = 10 ** 9 + 7
#         cache = {}

#         def count(n, k):
#             if not n:
#                 return 1 if k == 0 else 0
#             if k < 0:
#                 return 0
            
#             if (n, k) in cache:
#                 return cache[(n, k)]
            
#             cache[(n, k)] = 0
#             for i in range(n):
#                 cache[(n, k)] = (cache[(n, k)] + count(n - 1, k - i)) % MOD
            
#             return cache[(n, k)]
        
#         return count(n, k)

#############################################################################

#### DP SOLN ################################################################
# class Solution:
#     def kInversePairs(self, n: int, k: int) -> int:
#         MOD = 10 ** 9 + 7
#         dp = [[0] * (k + 1) for _ in range(n + 1)]
#         dp[0][0] = 1

#         for N in range(1, n + 1):
#             for K in range(0, k + 1):
#                 for pairs in range(N):
#                     if K - pairs >= 0:
#                         dp[N][K] += dp[N - 1][K - pairs]
        
#         return dp[n][k]

###############################################################################

####### SLIDING WINDOW ########################################################

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        prev = [0] * (k + 1)
        prev[0] = 1

        for N in range(1, n + 1):
            cur = [0] * (k + 1)
            total = 0
            for K in range(0, k + 1):
                if K >= N:
                    total -= prev[K - N]
                total = (total + prev[K]) % MOD
                cur[K] = total
            prev = cur
        
        return prev[k]
#################################################################################
s = Solution()
print(s.kInversePairs(3, 1))