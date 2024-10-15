import heapq
from typing import List
from math import ceil

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        heap = [-num for num in nums]
        heapq.heapify(heap)
        while k:
            num = heapq.heappop(heap)
            res += -num
            heapq.heappush(heap, -ceil(-num / 3))
            k -= 1
        return res

s = Solution()
nums = [1, 10, 3, 3, 3]
k = 3
print(s.maxKelements(nums, k))