from collections import deque
from typing import List

### MY SOLN #######################################################
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        max_digits = max(len(str(low)), len(str(high)))
        min_digits = min(len(str(low)), len(str(high)))
        
        possible = []

        def backtrack(string, curr, min_digit, max_digit):
            if not int(curr) or len(string) > max_digit:
                return 
            string += curr
            curr = str(int(curr) + 1) if curr != '9' else '0'
            if min_digit <= len(string) <= max_digit:
                possible.append(int(string))
            backtrack(string, curr, min_digit, max_digit)
        
        for i in range(1, 10):
            backtrack("", str(i), min_digits, max_digits)

        possible.sort()

        for num in possible:
            if low <= num<= high:
                res.append(num)

        return res
######################################################################

### OPTIMISED SOLN (nlogn) ###########################################
class Solution:
    def sequentialDigits(self, low, high):
        a = []

        for i in range(1, 9):
            num = i
            next_digit = i + 1

            while num <= high and next_digit <= 9:
                num = num * 10 + next_digit
                if low <= num <= high:
                    a.append(num)
                next_digit += 1

        a.sort()
        return a
######################################################################

### ANOTHER SOLN #####################################################
class Solution:
    def sequentialDigits(self, low, high):
        res = []
        queue = deque(range(1, 10))

        while queue:
            n = queue.popleft()
            if n > high:
                continue
            if low <= n <= high:
                res.append(n)
            ones = n % 10
            if ones < 9:
                queue.append(n * 10 + (ones + 1))
        
        return res
#######################################################################
s = Solution()
print(s.sequentialDigits(100, 300))

