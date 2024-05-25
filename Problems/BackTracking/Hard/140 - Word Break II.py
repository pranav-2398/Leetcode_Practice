from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def helper(i, part):
            if i >= len(s):
                res.append(" ".join(part))

            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    part.append(word)
                    helper(i + len(word), part)
                    part.pop()

        helper(0, [])

        return res
    
soln = Solution()
s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(soln.wordBreak(s, wordDict))