import heapq
from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = [(t[0], t[1], i) for i, t in enumerate(times)]
        times.sort()

        usedchairs = [] #(l, chair)
        availablechairs = [ i for i in range(len(times))] #chair

        for a, l, i in times:
            while usedchairs and usedchairs[0][0] <= a:
                leave, chair = heapq.heappop(usedchairs)
                heapq.heappush(availablechairs, chair)
            
            chair = heapq.heappop(availablechairs)
            heapq.heappush(usedchairs,(l, chair))

            if i == targetFriend:
                return chair