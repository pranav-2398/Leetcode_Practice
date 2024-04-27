from collections import defaultdict


### RECURSIVE SOLN #########################################
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        cache = {}

        def helper(r, k):
            if k == len(key):
                return 0
            if (r, k) in cache:
                return cache[(r, k)]
            
            res = float("inf")
            for i, c in enumerate(ring):
                if c == key[k]:
                    min_dist = min(
                        abs(r - i),
                        len(ring) - abs(r - i)
                    )
                    res = min(
                        res,
                        min_dist + 1 + helper(i, k + 1)
                    )
            
            cache[(r, k)] = res
            return res
        
        return helper(0, 0)

######## DP SOLN ###########################################
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = [0] * len(ring)
        
        for k in reversed(range(len(key))):
            next_dp = [float("inf")] * len(ring)
            for r in range(len(ring)):
                for i, c in enumerate(ring):
                    if c == key[k]:
                        min_dist = min(
                            abs(r - i),
                            len(ring) - abs(r - i)
                        )
                        next_dp[r] = min(
                            next_dp[r],
                            min_dist + 1 + dp[i]
                        )
            dp = next_dp
        
        return dp[0]
############################################################

s = Solution()
ring = "pqwcx"
key = "cpqwx"
print(s.findRotateSteps(ring, key))
                    
