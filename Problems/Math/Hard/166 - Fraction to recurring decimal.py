class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0:
            return 'Undefined'
        if numerator == 0:
            return '0'
        if numerator % denominator == 0:
            return str(numerator / denominator)
        
        neg = True if numerator * denominator < 0 else False
        numerator = abs(numerator)
        denominator = abs(denominator)

        output = ""
        output += "-" if neg else ""
        output += str(numerator // denominator)
        output += "."

        num_q = []
        while True:
            rem = numerator % denominator
            if rem == 0:
                for element in num_q:
                    output += str(element[-1])
                break
            numerator = rem * 10
            q = numerator // denominator

            if [numerator, q] not in num_q:
                num_q.append([numerator, q])
            else:
                ind = num_q.index([numerator, q])
                for element in num_q[:ind]:
                    output += str(element[-1])

                output += "("
                for element in num_q[ind:]:
                    output += str(element[-1])
                output += ')'
                break
        
        return output

s = Solution()
print(s.fractionToDecimal(1, 3))