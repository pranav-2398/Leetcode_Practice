from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        res = 0

        for i in range(N-1):
            a = 0
            for j in range(i + 1, N):
                a ^= arr[j - 1]
                b = 0
                for k in range(j, N):
                    b ^= arr[k]
                    if a == b:
                        res += 1
        
        return res