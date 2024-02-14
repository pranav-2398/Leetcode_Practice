################ MISC ##################################################

# from collections import deque


# class Solution:
#     def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
#         def encoding(s):
#             queue = deque([])
#             counter = 0

#             string = ''
#             i = 0

#             queue.append(s[0])

#             while queue:
#                 if i >= len(s):
#                     if counter > 1:
#                         string += queue.pop() + str(counter)
#                     else:
#                         string += queue.pop()
#                 else:
#                     if s[i] == queue[-1]:
#                         counter += 1
#                     else:
#                         if counter > 1:
#                             string += queue.pop() + str(counter)
#                         else:
#                             string += queue.pop()
#                         queue.append(s[i])
#                         counter = 1
#                     i += 1

#             return string

###################################################################################

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        cache = {}

        def count(i, k, prev, prev_count):
            if (i, k, prev, prev_count) in cache:
                return cache[(i, k, prev, prev_count)]
            
            if k < 0:
                return float("inf")
            if i == len(s):
                return 0
            
            if s[i] == prev:
                incr = 1 if prev_count in [1, 9, 99] else 0
                res = incr + count(i+1, k, prev, prev_count + 1)
            else:
                res = min(
                    count(i+1, k-1, prev, prev_count), #Delete s[i]
                    1 + count(i+1, k, s[i], 1) #Dont delete
                )
            cache[(i, k, prev, prev_count)] = res
            return res
        
        return count(0, k, "", 0)

s = Solution()
print(s.getLengthOfOptimalCompression('aaaaaaaaaaa', 2))
            
            

