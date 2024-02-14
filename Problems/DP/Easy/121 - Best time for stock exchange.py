from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_price = prices[0]
        max_profit = 0

        for price in prices:
            profit = price - curr_price

            if profit < 0:
                curr_price = price
            elif profit > max_profit:
                max_profit = profit

        return max_profit
    
s = Solution()
# prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]
print(s.maxProfit(prices))
