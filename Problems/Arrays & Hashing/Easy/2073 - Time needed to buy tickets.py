from collections import deque
from typing import List

##### MY SOLN ######################################################
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        queue = deque([(i,j) for i, j in enumerate(tickets)])
        while queue:
            pos, no_ticket = queue.popleft()
            res += 1
            no_ticket -= 1
            if no_ticket:
                queue.append((pos, no_ticket))
            elif pos == k:
                return res
#####################################################################
            
#### ANOTHER VERSION OF MY SOLN #####################################
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        queue = deque(range(len(tickets)))
        while queue:
            pos = queue.popleft()
            res += 1
            tickets[pos] -= 1
            if tickets[pos]:
                queue.append(pos)
            elif pos == k:
                return res
#####################################################################
            
### ONE PASS SOLN ##########################################################################
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        
        for i in range(len(tickets)):
            # If the current person is before or at the desired person 'k'
            if i <= k:
                # Buy the minimum of tickets available at person 'k' and the current person
                time += min(tickets[k], tickets[i])
            else:
                # If the current person is after 'k', buy the minimum of 
                # (tickets available at person 'k' - 1) and the current person
                time += min(tickets[k] - 1, tickets[i])
        
        return time
###############################################################################################

s = Solution()
# tickets = [2, 3, 2]
tickets = [5, 1, 1, 1]
print(s.timeRequiredToBuy(tickets, k = 0))