class Solution:
    def myAtoi(self, s: str) -> int:
        
        wsflag = False
        MIN = -2147483648
        MAX = 2147483647

        res, multiplier = '', 1

        s = s.strip()
        i = 0

        if not s:
            return 0

        if s[0] in ('-', '+'):
            multiplier = -1 if s[0] == '-' else 1
            i = 1
        elif not s[0].isnumeric():
            return 0
        
        for j in range(i, len(s)):
            if s[j].isdigit():
                res += s[j]
            else:
                break

        if res == '':
            return 0
        else:
            no = int(res) * multiplier
            if no > MAX:
                return MAX
            elif no < MIN:
                return MIN
            else:
                return no
        
s = Solution()
word = "   -42"
print(s.myAtoi(word))