from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        count = Counter(letters)

        word_scores = []
        for word in words:
            word_score = sum(score[ord(char) - ord('a')] for char in word)
            word_scores.append(word_score)
            
        def can_form_word(word, word_dict):
            word_count = Counter(word)
            for l in word:
                if word_dict[l] < word_count[l]:
                    return False
                
            return True

        def helper(i, count, score):
            if i >= len(words):
                return score
            
            max_score = 0
            #Include Word
            if can_form_word(words[i], count):
                for l in words[i]:
                    count[l] -= 1
                max_score = helper(i + 1, count, score + word_scores[i])

                for l in words[i]:
                    count[l] += 1
                max_score = max(max_score, helper(i + 1, count, score))
            
            else:
                max_score = helper(i + 1, count, score)

            return max_score
            
        return helper(0, count, 0)

s = Solution()
words = ["leetcode"]
letters = ["l","e","t","c","o","d"]
score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
print(s.maxScoreWords(words, letters, score))