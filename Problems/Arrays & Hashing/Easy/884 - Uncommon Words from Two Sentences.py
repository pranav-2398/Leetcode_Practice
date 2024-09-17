from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, A, B):
        count = Counter(A.split(" "))
        count += Counter(B.split(" "))

        return [word for word in count if count[word] == 1]