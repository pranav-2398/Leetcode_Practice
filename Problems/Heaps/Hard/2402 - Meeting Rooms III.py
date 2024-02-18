import heapq
from typing import List

### MY SOLN (Prepones the meeting if room is available which is not needed) #####
# class Solution:
#     def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
#         meetings.sort(key = lambda x:x[0])
#         duration = list(map(lambda x: x[1] - x[0], meetings))

#         end_time = []
#         count = [0] * n
#         res = [0, 1]

#         for i in range(min(n, len(meetings))):
#             heapq.heappush(end_time, (meetings[i][1], i))
#             count[i] += 1
        
#         for i in range(n, len(meetings)):
#             meeting_end, room_no = heapq.heappop(end_time)
#             heapq.heappush(end_time, (meeting_end + duration[i], room_no))
#             count[room_no] += 1
#             if count[room_no] >res[1]:
#                 res[0] = room_no
#                 res[1] = count[room_no]
#             elif count[room_no] == res[1] and room_no < res[0]:
#                 res[0] = room_no
#         return res[0]

##################################################################################
    
### SOLN #########################################################################
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        busy = []
        available = [i for i in range(n)]

        count = [0] * n
        meetings.sort()

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _end, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            
            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                time, room = heapq.heappop(busy)
                heapq.heappush(busy, (time + end - start, room))
            
            count[room] += 1
        
        return count.index(max(count))

###################################################################################
s = Solution()
# meetings = [[0,10],[1,5],[3,4], [2,7]]
meetings = [[0,10],[1,2],[12,14],[13,15]]
# print(meetings)
n = 2
print(s.mostBooked(n, meetings))

