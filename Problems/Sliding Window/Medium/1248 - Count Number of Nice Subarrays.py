from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = 0
        l, m = 0, 0
        res = 0
        for r in range(len(nums)):
            if nums[r] % 2:
                odd_count += 1

            while odd_count > k:
                if nums[l] % 2:
                    odd_count -= 1
                l += 1
                m = l
            
            if odd_count == k:
                while not nums[m] % 2:
                    m += 1
                res += (m - l) + 1

        return res
    
s = Solution()
# nums = [2,2,2,1,2,2,1,2,2,2]
nums = [1,1,2,1,1]
k = 2
print(s.numberOfSubarrays(nums, k))