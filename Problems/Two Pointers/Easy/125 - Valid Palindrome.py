class Solution:
    ########## MY SOLN #############################################################

    # def isPalindrome(self, s: str) -> bool:
    #     s = s.lower()
    #     l = 0 
    #     r = len(s) - 1

    #     while l <= r:
    #         if ord(s[l]) not in range(97, 123) and ord(s[l]) not in range(48, 58):
    #             l += 1
    #             continue
    #         if ord(s[r]) not in range(97, 123) and ord(s[r]) not in range(48, 58):
    #             r -= 1
    #             continue

    #         if s[l] != s[r]:
    #             return False
            
    #         l += 1
    #         r -= 1

    #     return True 

    ##################################################################################

    ####### ANOTHER SOLN #############################################################

    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True
    
    ###################################################################################

s = Solution()
sc = "ab2a"
print(s.isPalindrome(sc))