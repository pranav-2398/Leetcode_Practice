from typing import List

#### EDITORAL SOLN ############################################
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        ans = start = max_elements_in_window = 0

        for end in range(len(nums)):
            if nums[end] == max_element:
                max_elements_in_window += 1
            while max_elements_in_window == k:
                if nums[start] == max_element:
                    max_elements_in_window -= 1
                start += 1
            ans += start
        return ans
################################################################

### NEETCODE WAY ################################################################
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_n, max_cnt = max(nums), 0
        l = res = 0
        for r in range(len(nums)):
            if nums[r] == max_n:
                max_cnt += 1
            
            while max_cnt > k or (l <= r and max_cnt == k and nums[l] != max_n):
                if nums[l] == max_n:
                    max_cnt -= 1
                l += 1
            
            if max_cnt == k:
                res += l + 1
        
        return res
###################################################################################

s=Solution()
nums = [4, 3, 7, 10, 2, 10, 1, 6, 10, 7, 10, 10, 9, 8, 3]
print(s.countSubarrays(nums, 3))