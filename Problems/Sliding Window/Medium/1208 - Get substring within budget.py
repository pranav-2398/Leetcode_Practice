class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]

        res = 0
        total_cost = 0
        start = 0

        for i in range(len(s)):
            total_cost += cost[i]
            while total_cost > maxCost:
                total_cost -= cost[start]
                start += 1
            res = max(res, i + 1 - start)
        return res 

soln = Solution()
s = "ujteygggjwxnfl"
t = "nstsenrzttikoy"
maxCost = 43
print(soln.equalSubstring(s, t, maxCost))