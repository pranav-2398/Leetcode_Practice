from collections import Counter

### Queue Soln ######################################
class Solution:
    def countStudents(self, students, sandwiches):
        cnt = Counter(students)
        while students and cnt[sandwiches[0]] > 0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                cnt[sandwiches[0]] -=1
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
        return len(students)
######################################################
    
#### Count Soln ######################################
class Solution:
    def countStudents(self, students, sandwiches):
        res = len(students)
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                return res
        
        return res
#######################################################

s = Solution()
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(s.countStudents(students, sandwiches))