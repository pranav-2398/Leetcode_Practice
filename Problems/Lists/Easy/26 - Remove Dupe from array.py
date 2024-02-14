from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        swap_index = 0
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != start:
                swap_index += 1
                nums[swap_index] = nums[i]
                counter += 1
                start = nums[i]
        return counter

nums = [0,0,1,1,1,2,2,3,3,4]  
s = Solution()

print(s.removeDuplicates(nums))
print(nums)

