class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        d = abs(dividend)
        dv = abs(divisor)

        output = 0

        while d >= dv:
            tmp = dv
            mul = 1
            while d >= tmp:
                d -= tmp
                output += mul
                mul += mul
                tmp += tmp
        
        if (dividend < 0 and divisor >= 0 ) or (dividend >= 0 and divisor < 0 ):
            output = -output

        return min(MAX, max(MIN, output))
    
s = Solution()
print(s.divide(10, 3))