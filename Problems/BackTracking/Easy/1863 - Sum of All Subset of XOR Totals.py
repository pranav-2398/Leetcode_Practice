from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
        
        def dfs(i, total):
            if i == N:
                return total
            
            return (
                dfs(i + 1, total ^ nums[i]) #Add element
                + dfs(i + 1, total) #Remove element
            ) 

        return dfs(0, 0)

s = Solution()
print(s.subsetXORSum([1, 3]))    