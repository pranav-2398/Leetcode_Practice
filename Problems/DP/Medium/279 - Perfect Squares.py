
from collections import defaultdict
import math


class Solution:
    def numSquares(self, n: int) -> int:
        m = int(math.sqrt(n))
        res = 0

        count = {}

        def returncount(n):
            if n in count:
                return count[n]
            temp_count= 0
            j = 0
            while ps_list[j] <= n:
                count[n] = min(count.get(n, float('inf')), 1 + count[n - ps_list[j]])
                j += 1

        # ps_set = set()
        ps_list = []
        for i in range(1, m+2):
            val = i * i
            # ps_set.add(val)
            ps_list.append(val)
            count[val] = 1
        
        for i in range(1, n+1):
            returncount(i)
        
        return count[n]

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n+1):
            for s in range(1, target + 1):
                sq = s * s
                if target - sq < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - sq])

        return dp[n]
s = Solution()
print(s.numSquares(12))

        