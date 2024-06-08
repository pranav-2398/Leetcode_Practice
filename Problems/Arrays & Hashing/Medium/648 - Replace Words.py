from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        res = []
        sentence = sentence.split(' ')
        dictionary.sort(key = len)
        for word in sentence:
            found = False
            for key in dictionary:
                if word[:len(key)] == key:
                    found = True
                    res.append(key)
                    break
            
            if not found:
                res.append(word)
        return " ".join(res)