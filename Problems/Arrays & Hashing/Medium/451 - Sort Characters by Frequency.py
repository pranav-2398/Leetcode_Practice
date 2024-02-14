from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = [(v,k) for k,v in Counter(s).items()]
        freq.sort(key=lambda x:x[0], reverse =True)
        return "".join([k*v for (v,k) in freq])

soln = Solution()
s = "tree"
print(soln.frequencySort(s))

