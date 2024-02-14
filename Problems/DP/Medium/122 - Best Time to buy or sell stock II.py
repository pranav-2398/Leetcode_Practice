from collections import defaultdict
from typing import List

#### MY SOLN ########################################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = defaultdict(int)

        if len(prices) < 2:
            return 0
        
        for i in range(len(prices) - 2, -1, -1):
            price = prices[i + 1] - prices[i]
            if price < 0:
                price = 0
            profit[i] = price + profit[i + 1]
        
        return profit[0]
#######################################################
    
### OPTIMISED SOLN ####################################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit

#########################################################