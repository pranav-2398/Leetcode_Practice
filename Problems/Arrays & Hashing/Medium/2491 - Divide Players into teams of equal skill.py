from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
       skill.sort()
       maxskill = skill[0] + skill[-1]
       res = 0
       l= 0
       r = len(skill) - 1
       while l < r:
        curskill = skill[l] + skill[r]
        if curskill != maxskill:
            return -1
        res += skill[l] * skill[r]
        l += 1
        r -= 1
       return res