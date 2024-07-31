from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        cache = {}
        def helper(i):
            if i == len(books):
                return 0 
            if i in cache:
                return cache[i]
            curwidth = shelfWidth
            maxheight = 0
            cache[i] = float("inf")
            for j in range(i, len(books)):
                width, height = books[j]
                if curwidth < width:
                    break
                curwidth -= width
                maxheight = max(maxheight, height)
                cache[i] = min(
                    cache[i],
                    helper(j + 1) + maxheight
                )
            return cache[i]
        return helper(0)
    
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4
s = Solution()
print(s.minHeightShelves(books, shelfWidth))