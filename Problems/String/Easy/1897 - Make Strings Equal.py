from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cache = {}

        for word in words:
            for x in word:
                cache[x] = cache.get(x, 0) + 1

        for k in cache.keys():
            if cache[k] % len(words) != 0:
                return False
            
        return True




x = 'abc'

y = list(x)
print(y)