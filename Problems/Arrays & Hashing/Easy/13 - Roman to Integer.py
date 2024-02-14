class Solution:

####### MY SOLUTION ########################################################
    # def romanToInt(self, s: str) -> int:
    #     symbols = {
    #         "I": 1,
    #         "V": 5,
    #         "X": 10,
    #         "L": 50,
    #         "C": 100,
    #         "D": 500,
    #         "M": 1000
    #     }

    #     num = 0

    #     for i in range(0, len(s)):
    #         if i != len(s) -1:
    #             if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
    #                 num += -1
    #             elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
    #                 num += -10
    #             elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
    #                 num += -100
    #             else:
    #                 num += symbols.get(s[i])
    #         else:
    #             num += symbols.get(s[i])

    #     return num
#####################################################################################
    
##### OPTIMISED SOLUTION #############################################################
    
    def romanToInt(self, s: str) -> int:
        alphabet = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        output = 0
        for i in range(len(s)):
            if i < len(s) - 1 and alphabet[s[i]] < alphabet[s[i + 1]]:
                output -=  alphabet[s[i]]
            else:
                output += alphabet[s[i]]
        return output
########################################################################################

soln = Solution()
print(soln.romanToInt('MCMXCIV'))


    