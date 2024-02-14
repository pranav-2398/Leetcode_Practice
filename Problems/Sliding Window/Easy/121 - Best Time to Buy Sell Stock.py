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