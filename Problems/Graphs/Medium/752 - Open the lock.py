from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        def children(lock):
            res = []
            for i in range(4):
                pos_digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + pos_digit + lock[i + 1:])
                neg_digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + neg_digit + lock[i + 1:])
            
            return res

        q = deque()
        q.append(["0000", 0]) #[lock, turns]
        visit = set(deadends)
        while q:
            lock, turn = q.popleft()
            if lock == target:
                return turn
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turn + 1])
        return -1