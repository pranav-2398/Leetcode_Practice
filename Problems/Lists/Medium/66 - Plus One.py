from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        def helper(nums, idx):
            if idx == 0:
                if nums[idx] == 9:
                    nums[idx] = 0
                    nums = [1] + nums
                else:
                    nums[idx] += 1
            else:
                if nums[idx] == 9:
                    # digits[idx] += 1
                    nums[idx] = 0
                    nums = helper(nums, idx - 1)
                else:
                    nums[idx] += 1
            return nums

        digits = helper(digits, len(digits)-1)

        return digits

s = Solution()
print(s.plusOne([9,9]))    