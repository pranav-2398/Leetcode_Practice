## MY SOLN ##########################################
class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        
        prefixsum = [0] * n
        prefixsum[0] = 1

        sufixsum = [0] * n
        sufixsum[-1] = n

        for i in range(1, n):
            prefixsum[i] = prefixsum[i - 1] + i + 1
        
        for i in range(n-2, 0, -1):
            sufixsum[i] = sufixsum[i + 1] + i + 1

        for i in range(n):
            if prefixsum[i] == sufixsum[i]:
                return i + 1
        
        return -1
######################################################

### OPTIMISED SOLN ###################################
class Solution:
    def pivotInteger(self, n: int) -> int:
        current_sum = 0
        nums = range(1, n + 1)
        total_sum = sum(nums)
        for num in nums:
            current_sum += num
            if current_sum == total_sum:
                return num
            total_sum -= num
        
        return -1
#######################################################

s = Solution()
print(s.pivotInteger(8))