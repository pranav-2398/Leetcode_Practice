class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {1:1, 0:1}

        def helper(n, dp):
            if not n in dp:
                dp[n] = helper(n-1, dp) + helper(n-2, dp)
            return dp[n]
        
        return helper(n, dp)

s = Solution()
print(s.climbStairs(38))


###### REJECTED SOLUTION (TIME LIMIT EXCEEDED) #######################################

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = {1:1, 0:1}

#         if not n in dp:
#             dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

#         return dp[n]
    
##################################################################