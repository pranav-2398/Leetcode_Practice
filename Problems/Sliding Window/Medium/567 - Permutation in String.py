from collections import Counter

### MY SOLN (TIME LIMIT EXCEEDED) #########################
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         count = Counter(s1)

#         i = 0 
#         while i < len(s2):
#             if s2[i] in count:
#                 count_copy = count.copy()
#                 j = i
#                 while s2[j] in count_copy and j < len(s2):
#                     if count_copy[s2[j]] <= 0:
#                         break
#                     count_copy[s2[j]] -= 1
#                     j += 1

#                 if not max(count_copy.values()):
#                     return True
#             i += 1
        
#         return False
#############################################################

### MY SOLN V2 ##############################################
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)

        for i in range(len(s2) - len(s1) + 1):
            count1 = Counter(s2[i:i + len(s1)])
            if count1 == count:
                return True
        
        return False
##############################################################
    
### OPTIMISED SOLN ###########################################
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count, s2count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if s1count[i] == s2count[i] else 0

        l = 0
        for i in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[i]) - ord('a')
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1
            
            l += 1
        return matches == 26


s = Solution()
print(s.checkInclusion('ab', 'eidbaooo'))