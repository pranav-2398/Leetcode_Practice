from collections import Counter

### MY SOLN (TIME EXCESS)###############################################################
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if len(s) < len(t): return ""

#         res = 'z' * (len(s) + 1) 
#         count_t = Counter(t)
#         index_s = []

#         for i in range(len(s)):
#             if s[i] in count_t:
#                 index_s.append(i)

#         if not index_s:
#             return ""

#         start = 0
#         end = 0

#         while start <= end:
#             word = s[index_s[start]:index_s[end] + 1]
#             word_count = Counter(word)
#             if all([word_count.get(key, 0) >= count_t[key] for key in count_t.keys()]):
#                 if len(word) < len(res):
#                     res = word
#                 start += 1
#             elif end == len(index_s) - 1:
#                 start += 1
#             else:
#                 end += 1 if end <= len(index_s) - 2 else 0
        
#         if res == 'z' * (len(s) + 1):
#             return ""
         
#         return res 
#########################################################################################
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, reslen = [-1, -1], float("inf")
        l = 0 
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = (r - l + 1)
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r + 1] if reslen != float('inf') else ""

########################################################################################
s = Solution()
char = "ADOBECODEBANC"
t = 'ABC'
print(s.minWindow(char, t))
