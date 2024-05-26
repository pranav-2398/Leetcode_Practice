from collections import defaultdict


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n == 1:
            return 3
        
        tmp = {
            (0, 0): 1, (0, 1): 1, (0, 2): 0,
            (1, 0): 1, (1, 1): 0, (1, 2): 0
        }

        for i in range(n - 1):
            res = defaultdict(int)

            #Choose P
            res[(0, 0)] = ((tmp[(0, 0)] + tmp[(0, 1)]) % MOD + tmp[(0, 2)]) % MOD
            res[(1, 0)] = ((tmp[(1, 0)] + tmp[(1, 1)]) % MOD + tmp[(1, 2)]) % MOD

            #Choose L
            res[(0, 1)] = tmp[(0, 0)]
            res[(0, 2)] = tmp[(0, 1)]
            res[(1, 1)] = tmp[(1, 0)]
            res[(1, 2)] = tmp[(1, 1)]

            #Choose A
            res[(1, 0)] = (res[(1, 0)] + ((tmp[(0, 0)] + tmp[(0, 1)]) % MOD + tmp[(0, 2)]) % MOD) % MOD
            tmp= res

        return sum(tmp.values()) % MOD