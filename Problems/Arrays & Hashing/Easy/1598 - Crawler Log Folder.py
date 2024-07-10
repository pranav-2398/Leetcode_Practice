from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0 
        for log in logs:
            if log == '../':
                res = (res - 1) if res else 0
            elif log == './':
                pass
            else:
                res += 1
        return res