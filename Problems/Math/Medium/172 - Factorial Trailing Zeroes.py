class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Idea is that multiplying with 10 gives you a trailing zero.
        10 is made of 2 and 5
        So we count min power of 2 and 5. 
        But Power of 2 will be always be greater than 5. 
        Hence we count power of 5

        1st we check for 5 then 25 then 125 till quotient becomes 0 as number 
        becomes smaller than that power
        """
        count = 0
        i = 5
        while True:
            res = int(n / i)
            if not res:
                break
            count += res
            i *= 5
        return count
    
