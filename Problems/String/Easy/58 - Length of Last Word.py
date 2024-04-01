##### MY SOLN ############################################################

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(list(filter(lambda x: len(x) > 0, s.split(" ")))[-1])


###########################################################################

### ANOTHER SOLN ##################################

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s.strip()
#         res = s.split(" ")
#         return len(res[-1])

####################################################

s = Solution()
print(s.lengthOfLastWord("   fly me   to   the moon  "))
