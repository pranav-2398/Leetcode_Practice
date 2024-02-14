from typing import List

### MY ORIGINAL SOLN (TIME EXCESS) ###########################
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        for i in range(k):
            for j in range(len(nums) - 1, 0, -1):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

###############################################################
                
### OPTIMISED SOLN ############################################
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def helper(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        #Reversing the whole string
        helper(0, len(nums) - 1)

        #Reversing 1st k elements
        helper(0, k - 1)

        #Reversing the remaining elements
        helper(k, len(nums) - 1)

###############################################################

