from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = float("inf")
        lastcost = 0
        lastlastcost = 0
        price = 0

        for i in range(len(cost)-1, -1, -1):
            price = min(cost[i] + lastcost, cost[i] + lastlastcost)
            lastlastcost = lastcost
            lastcost = price
            if i <= 1:
                mincost = min(price, mincost)
        
        return mincost

s = Solution()
cost = [1,100,1,1,1,100,1,1,100,1]
print(s.minCostClimbingStairs(cost))