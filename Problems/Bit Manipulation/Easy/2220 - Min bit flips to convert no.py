## MY SOLN################################################################
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        startbin = "{0:b}".format(start)
        goalbin = "{0:b}".format(goal)
        
        res = 0
        for i in range(max(len(startbin), len(goalbin))):
            val = (start ^ goal) & 1
            if val:
                res += 1
            start = start >> 1
            goal = goal >> 1
        
        return res
## ANOTHER SOLN##########################################################
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR to find differing bits
        xor_result = start ^ goal
        count = 0
        # Count the number of 1s in xor_result (differing bits)
        while xor_result:
            count += xor_result & 1  # Increment if the last bit is 1
            xor_result >>= 1  # Shift right to process the next bit
        return count
#########################################################################