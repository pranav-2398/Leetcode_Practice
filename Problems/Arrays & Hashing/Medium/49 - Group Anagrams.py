from collections import defaultdict
from typing import List

### MY SOLN #####################################################
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)
        strs.sort(key=len)

        res = []

        for st in strs:
            charset = "".join(sorted(list(st)))
            cache[charset].append(st)

        for k in cache.keys():
            res.append(cache[k])

        return res
##################################################################
    
### OPTIMISED SOLN ###############################################
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            cache[tuple(count)].append(s)

        return cache.values
####################################################################
s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))
    
# st = 'eat'
# print("".join(sorted(list(st))))