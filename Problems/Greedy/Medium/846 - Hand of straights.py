from collections import Counter
import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        
        minh = list(count.keys())
        heapq.heapify(minh)

        while minh:
            first = minh[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1

                if not count[i]:
                    if i != minh[0]:
                        return False
                    heapq.heappop(minh)
        return True
    
s = Solution()
# hand = [1,2,3,6,2,3,4,7,8]
hand = [8, 10, 12]
# groupsize = 3
groupsize = 3
print(s.isNStraightHand(hand, groupsize))

            