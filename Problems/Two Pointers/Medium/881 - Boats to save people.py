from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l, r = 0, len(people) - 1
        while l <= r:
            res += 1
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1        
        return res
    
s = Solution()
people = [3,2,2,1]
limit = 3
print(s.numRescueBoats(people, limit))