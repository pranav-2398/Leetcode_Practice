############# NON DP SOLN ##########################################
# class Solution:   
#     def longestPalindrome(self, s: str) -> str:
#         res = ""
#         reslen = 0

#         # Reason why there are 2 while loops is because for even 
#         # characters, res will give out if not both of them kept 
#         # together as 1st while will consider 2 digits but second will 
#         # consider one character as start which can handle cases like 'ac' 

#         for i in range(len(s)):
#         # even length 
#             l, r = i, i + 1
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r - l + 1) > reslen:
#                     reslen = r - l + 1
#                     res= s[l:r+1]
#                 l -= 1
#                 r += 1

#         # Odd length
#             l, r = i, i
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r - l + 1) > reslen:
#                     reslen = r - l + 1
#                     res = s[l:r+1]
#                 l -= 1
#                 r += 1
    
#         return res
###################################################################
                
#### DP SOLN ######################################################
class Solution:   
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        maxlen = 1
        maxstr = s[0]

        n = len(s)
        dp = []

        for _ in range(n):
            dp.append([None]*n)

        for i in range(n):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i - j + 1 > maxlen:
                        maxlen = i - j + 1
                        maxstr = s[j:i+1]
        return maxstr
####################################################################

s = Solution()
word = "babad"

print(s.longestPalindrome(word))
