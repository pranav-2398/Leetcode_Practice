from typing import List

################ ORIGINAL SOLN #########################
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        i = j = 0
        res = 0
        while j < len(bank):
            if i == j:
                j += 1
            else:
                count1 = bank[i].count('1')
                if not count1:
                    i += 1
                else: 
                    count2 = bank[j].count('1')
                    if not count2:
                        j += 1
                    else:
                        res += count1 * count2
                        i = j
                        j += 1
        
        return res
##########################################################
    
##### SYNTACTICALLY BETTER SOLN ##########################
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = bank[0].count('1')
        res = 0

        for i in range(1, len(bank)):
            curr = bank[i].count('1')
            if curr:
                res += prev * curr
                prev = curr
        
        return res

############################################################

s = '011001'
print([sum(int(i) for i in s)][0])
