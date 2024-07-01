from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        l = 0
        r = 0
        cnt = 0

        for r in range(len(arr)):
            cnt += 1 if arr[r] % 2 else 0
            length = r - l + 1

            if length > 3:
                cnt -= 1 if arr[l] % 2 else 0
                l += 1
                length -= 1
            
            if length == 3 and cnt == 3:
                return True
        
        return False