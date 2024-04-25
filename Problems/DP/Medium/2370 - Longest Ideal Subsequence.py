### MY SOLN ########################################################
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        res = 1
        dp = [1] * len(s)
        dp[len(s) - 1] = 1

        mapset = {s[-1] : len(s) - 1}

        for i in range(len(s) - 2, -1, -1):
            current_word = s[i]
            temp = dp[i]
            for j in range(-k, k + 1):
                string = chr(ord(current_word) + j)
                if string in mapset:
                    temp = max(temp, dp[i] + dp[mapset[string]])
            dp[i] = temp
            mapset[current_word] = i
            res = max(res, dp[i])
        
        return res
#### RECURSIVE SOLN ##############################################
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        cache = {}

        def helper(i, prev):
            if i == len(s):
                return 0
            if (i, prev) in cache:
                return cache[(i, prev)]
            
            res = helper(i + 1, prev) #skip s[i]

            if prev == '' or abs(ord(s[i]) - ord(prev)) <= k :
                res = max(res, 1 + helper(i + 1, s[i])) #include s[i]
            
            cache[(i, prev)] = res
            return res
        
        return helper(0, "")
######################################################################

sol = Solution()
s = "acfgbd"
k = 2
print(sol.longestIdealString(s, k))