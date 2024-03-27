from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        res = 0 
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i + 1
        
        return start
                    
s = Solution()
gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
print(s.canCompleteCircuit(gas, cost))
