from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        Cword1 = Counter(word1)
        Cword2 = Counter(word2)

        n1 = Counter(Cword1.values())
        n2 = Counter(Cword2.values())

        return Cword1 == Cword2 or (n1 == n2 and Cword1.keys() == Cword2.keys())