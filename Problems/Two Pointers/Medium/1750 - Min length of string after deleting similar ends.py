#### MY SOLN #############################################
class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        strlist = list(s)


        while l < r:
            if l != r and s[l] == s[r]:
                l += 1
                r -= 1
            elif l > 0 and s[l] == s[l - 1]:
                l += 1
            elif r < len(s) - 1 and s[r] == s[r + 1]:
                r -= 1
            else:
                break
        
        return 1 + r - l
#########################################################
    
##### OPTIMISED SOLN ####################################
class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        strlist = list(s)


        while l < r and s[l] == s[r]:
            tmp = s[l]
            while l <= r and s[l] == tmp:
                l += 1
            while l <= r and s[r] == tmp:
                r -= 1
        
        return 1 + r - l
##########################################################
    
s = Solution()
print(s.minimumLength("abbbbbbbbbbbbbbbbbbba"))