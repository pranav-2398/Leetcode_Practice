class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        val = time // (n - 1)
        if not val % 2:
            return 1 + (time % (n - 1))
        else:
            return n - (time % (n - 1))