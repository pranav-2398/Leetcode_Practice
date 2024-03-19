import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for num in nums:
            heapq.heappush(res, num)

            if len(res) > k:
                heapq.heappop(res)
        
        return res[0]

s = Solution()
nums = [3,2,1,5,6,4]
print(s.findKthLargest(nums, 2))