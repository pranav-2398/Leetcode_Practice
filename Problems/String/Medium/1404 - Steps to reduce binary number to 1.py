class Solution:
    def numSteps(self, s: str) -> int:
        number = 0
        s = "".join(reversed(s))
        
        for i in range(len(s)):
            number += int(s[i]) * (2 ** i)

        steps = 0
        while number != 1:
            if not number % 2:
                number = number // 2
            else:
                number += 1
            steps += 1

        return steps 
    
soln = Solution()
s = '1101'
print(soln.numSteps(s))