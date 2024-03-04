from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        mscore = 0

        tokens.sort()

        if power < tokens[0]:
            return 0

        l, r = 0, len(tokens) - 1

        while l <=r:
            if not score or tokens[l] <= power:
                power -= tokens[l]
                score += 1
                l += 1
            elif score >= 1 and tokens[l] > power:
                power += tokens[r]
                score -= 1
                r -= 1
            mscore = max(score, mscore)
            
        return mscore
            
s = Solution()
tokens = [200,100]
power = 150
print(s.bagOfTokensScore(tokens, power))