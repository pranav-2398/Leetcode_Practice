from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = dict(Counter(s))
        counter_t = dict(Counter(t))

        res = 0

        for s_char in counter_s.keys():
            s_count = counter_s[s_char]
            t_count = counter_t.get(s_char, 0)

            if s_count > t_count:
                res += s_count - t_count

        return res