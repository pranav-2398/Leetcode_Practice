from collections import Counter
import heapq

class Solution:
    def minimumPushes(self, word: str) -> int:
        countword = Counter(word)
        heap = [-v for k, v in countword.items()]
        heapq.heapify(heap)
        
        letters = 8
        i = 1
        res = 0
        while heap:
            value = heapq.heappop(heap)
            res += i * (-value)
            letters -= 1
            if not letters:
                i += 1
                letters = 8
        return res

s = Solution()
word = "alporfmdqsbhncwyu"
print(s.minimumPushes(word))