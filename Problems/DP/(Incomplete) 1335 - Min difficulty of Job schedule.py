from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        if len(jobDifficulty) < d:
            return -1 
        
        if len(jobDifficulty) == d:
            return sum(jobDifficulty)
        
        def helper(nums, d):
            if d <= 0 and nums:
                return max(nums) 
            elif d <= 0 :
                return 0
            
            if d-1 != 0:
                val1 = helper(nums[:(-1 * (d-1))], 0) + helper(nums[(-1 * (d-1)):], d-2)
            else:
                val1 = float('inf')

            val2 = helper(nums[:(-1 * d)], 0) + helper(nums[(-1 * d):], d-1)

            return min(val1, val2)
        
        return helper(jobDifficulty, d)

s = Solution()
# jobDifficulty = [6, 5, 4, 3, 2, 1]
jobDifficulty = [9, 9, 9]
print(s.minDifficulty(jobDifficulty, 4))