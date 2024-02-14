from collections import Counter
import math
from typing import List

########## MY SOLN ####################################
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cache = {}

        for num in nums:
            cache[num] = cache.get(num, 0) + 1


        res = 0
        for k in cache.keys():
            while cache[k] > 0:
                if cache[k] % 3 == 0:
                    res += cache[k] // 3
                    cache[k] = 0
                elif cache[k] - 3 >= 2:
                    res += 1
                    cache[k] -= 3
                elif cache[k] % 2 == 0:
                    res += cache[k] // 2
                    cache[k] = 0
                else:
                    return -1
        
        return res

##########################################################
    

###### OPTIMISED SOLN ####################################
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0

        for n, c in count.items():
            if c == 1:
                return -1
            res += math.ceil(c / 3)

        # Reason why we take ceil of 3 is coz if you take 12 , it takes 4 steps as 12 / 3 as 3 + 3 + 3 + 3 
            # But if you take 13 which 3 + 3 +  3  + 2 + 2  Essentially, one 3 in 12 with 2 twos
            # Similarly for 14, which 3 + 3 + 3 + 3 + 2 , Replaced one 2 in 13 with a 3 
            # So , no of operations will always be n / 3 + 1
        
        return res

###########################################################
    
#### DP SOLN ##############################################
    
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cache = {}

        def dfs(n):
            if n < 0:
                return float('inf')
            if n in [2, 3]:
                return 1
            if n in cache:
                return cache[n]
            
            res = min(dfs(n-2), dfs(n-3))
            if res == -1:
                return -1
            cache[n] = res + 1
            return res + 1
        
        count = Counter(nums)
        res = 0
        
        for n, c in count.items():
            op = dfs(c)
            if op == float('inf'):
                return -1 
            res += op
        
        return res

##############################################################


s = Solution()
# nums = [2,3,3,2,2,4,2,3,4]
nums = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]
print(s.minOperations(nums))