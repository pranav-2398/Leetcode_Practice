from collections import defaultdict
from typing import List

### MY ORIGINAL SOLN #############################################
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        num_dict = defaultdict(int)
        k_list = []

        for num in nums:
            if num not in num_dict:
                if not len(k_list):
                    k_list.append({num})
                else:
                    k_list[0].add(num)
                num_dict[num] += 1
            else:
                num_dict[num] += 1
                k_list[num_dict[num] - 2].remove(num)
                if len(k_list) >= num_dict[num]:
                    k_list[num_dict[num] - 1].add(num)
                else:
                    k_list.append({num})
        
        i = len(k_list) - 1
        while k > 0:
            if not k_list[i]:
                pass
            else:
                res.extend(list(k_list[i]))
                k -= len(k_list[i])
            i -= 1
        
        return res
#######################################################################
    
### LESS CODE SOLN (SAME LOGIC AS MINE)##################################
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(nums) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
#######################################################################

s = Solution()
# nums = [1,1,1,2,2,3]
nums = [5,3,1,1,1,3,73,1]
print(s.topKFrequent(nums, 2))
