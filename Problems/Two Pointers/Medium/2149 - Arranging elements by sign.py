from collections import deque
from typing import List

## MY SOLN #################################################
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [-1]
        stack = deque()
        for num in nums:
            if res[-1] * num < 0:
                res.append(num)
                if stack and num * stack[0] < 0:
                    res.append(stack.popleft())
            else:
                stack.append(num)
        return res[1:]
#############################################################
    
## ANOTHER SOLN #############################################
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        res = [0] * len(nums)

        for k in range(len(nums)):
            if nums[k] > 0:
                res[i] = nums[k]
                i += 2
            else:
                res[j] = nums[k]
                j += 2
        
        return res

##############################################################
s = Solution()
# nums = [3,1,-2,-5,2,-4]
nums = [-1, 1]
print(s.rearrangeArray(nums))