from collections import Counter
import heapq
from typing import List

### MY SOLN ##########################################################
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counterx = Counter(arr)

        count_list = [[k,v] for k, v in counterx.items()]
        count_list.sort(key = lambda x: x[1],reverse = True)
        
        i = len(count_list) - 1
        while k > 0 and i >= 0:
            count_list[i][1] -= 1
            k -= 1
            if not count_list[i][1]:
                count_list.pop()
                i -= 1

        return len(count_list)
######################################################################

## OTHER SOLN (USING HEAPS) ##########################################
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        heap = list(freq.values())
        heapq.heapify(heap)
        
        res = len(heap)
        while k > 0 and heap:
            f = heap.heappop(heap)
            if k >= f:
                k -= f
                res -= 1
        return res
#######################################################################

#### O(n) Solution ####################################################
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        freq_list = [0] * (len(arr) + 1) #freq -> # of elements w that freq

        for n, f in freq.items():
            freq_list[f] += 1

        res = len(freq)
        for f in range(1, len(freq_list)):
            remove = freq_list[f]
            if k >= f * remove:
                k -= f * remove
                res -= remove
            else:
                remove = k // f
                res -= remove
                break
        return res
######################################################################
s = Solution()
arr = [2,4,1,8,3,5,1,3]
print(s.findLeastNumOfUniqueInts(arr, 3))