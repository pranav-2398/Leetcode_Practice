from collections import Counter
import heapq
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False

        count = Counter(nums)
        
        minh = list(count.keys())
        heapq.heapify(minh)

        while minh:
            first = minh[0]

            for i in range(first, first + k):
                if i not in count:
                    return False
                count[i] -= 1

                if not count[i]:
                    if i != minh[0]:
                        return False
                    heapq.heappop(minh)
        return True