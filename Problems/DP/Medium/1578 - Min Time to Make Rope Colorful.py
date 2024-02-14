from typing import List

####### MY SOLUTION ##############################################

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        i = 0 
        j = 1

        while (i < len(colors) - 1 and j <= len(colors) - 1):
            if colors[i] == colors[j]:
                if neededTime[i] < neededTime[j]:
                    res += neededTime[i]
                    i = j
                    j += 1
                else:
                    res += neededTime[j]
                    j += 1
            else:
                i = j
                j += 1
    
        return res

#####################################################################

########## DIFFERENT SOLUTION #######################################
    
# class Solution:
#     def minCost(self, colors: str, neededTime: List[int]) -> int:
#         totalTime = 0
#         i = 0
#         j = 0

#         while i < len(neededTime) and j < len(neededTime):
#             currTotal = 0
#             currMax = 0

#             while j < len(neededTime) and colors[i] == colors[j]:
#                 currTotal += neededTime[j]
#                 currMax = max(currMax, neededTime[j])
#                 j += 1

#             totalTime += currTotal - currMax
#             i = j

#         return totalTime

########################################################################
    

s = Solution()

colorlist = ['abaac', 'abc', 'aabaa', 'aaabbbabbbb']
neededTimelist = [[1,2,3,4,5], [1,2,3], [1,2,3,4,1], [3,5,10,7,5,3,5,5,4,8,1]]

# colorlist = ['aaabbbabbbb']
# neededTimelist = [[3,5,10,7,5,3,5,5,4,8,1]]

for color, neededTime in zip(colorlist, neededTimelist):
    print(s.minCost(color, neededTime))
