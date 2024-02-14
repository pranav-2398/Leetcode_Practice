from typing import List

class Solution:
    ###### MY SOLUTION ###################################################
    # def generate(self, numRows: int) -> List[List[int]]:
    #     pascals = [[1],[1,1]]

    #     for i in range(2, numRows):
    #         pascals.append([])
    #         pascals[i].append(1)
    #         for j in range(1, i):
    #             pascals[i].append(pascals[i-1][j-1] + pascals[i-1][j])
    #         pascals[i].append(1)
        
    #     return pascals[:numRows]
    
    ########################################################################

    ############# ANOTHER SOLN #############################################
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res
    #########################################################################
    
s = Solution()
print(s.generate(3))

        