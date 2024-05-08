import heapq
from typing import List


### MY SOLN ####################################################
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = [[sc, i] for i, sc in enumerate(score)]
        score.sort(reverse = True)

        for i in range(len(score)):
            if i == 0:
                score[i][0] = "Gold Medal"
            elif i == 1:
                score[i][0] = "Silver Medal"
            elif i == 2:
                score[i][0] = "Bronze Medal"
            else:
                score[i][0] = str(i + 1)

        score.sort(key = lambda x: x[1])
        return [sc for sc, i in score]

###### HEAP SOLN ##################################################
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)

        # Create a heap of pairs (score, index)
        heap = []
        for index, score in enumerate(score):
            heapq.heappush(heap, (-score, index))
        
        # Assign ranks to athletes
        rank = [0] * N
        place = 1
        while heap:
            original_index = heapq.heappop(heap)[1]
            if place == 1:
                rank[original_index] = "Gold Medal"
            elif place == 2:
                rank[original_index] = "Silver Medal"
            elif place == 3:
                rank[original_index] = "Bronze Medal"
            else:
                rank[original_index] = str(place)
            place +=1
            
        return rank

###################################################################