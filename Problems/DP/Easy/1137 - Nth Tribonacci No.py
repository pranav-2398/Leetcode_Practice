class Solution:
    def tribonacci(self, n: int) -> int:
        res = [0, 1, 1]

        if n <= 2:
            return res[n]

        for i in range(3, n + 1):
            ans = sum(res)
            res[0] = res[1]
            res[1] = res[2]
            res[2] = ans

        return ans