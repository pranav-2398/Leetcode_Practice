### MY ORIGINAL SOLN #################################################
class Solution:
    def countAndSay(self, n: int) -> str:
        return self.helper(n)

    def helper(self, n):
        if n == 1:
            return '1'
        
        currstr = self.helper(n-1) 
        res = []
        
        res.append({currstr[0] : 1})
        j = 0
        for i in range(1, len(currstr)):
            if currstr[i] == currstr[i - 1]:
                res[j][currstr[i]] = res[j].get(currstr[i], 0) + 1
            else:
                res.append({currstr[i] : 1})
                j += 1
        
        word = ''

        for i in res:
            for k, v in i.items():
                word += str(v) + str(k)

        return word
    
########################################################################
    
### OPTIMISED SOLN #####################################################
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        currstr = self.countAndSay(n-1) 
        res = ""
        ct = 1
        for i in range(len(currstr)):
            if i == len(currstr) - 1 or currstr[i] != currstr[i + 1]:
                res += str(ct) + currstr[i]
                ct = 1
            else:
                ct += 1

        return res

########################################################################
    
s = Solution()
print(s.countAndSay(4))


                

