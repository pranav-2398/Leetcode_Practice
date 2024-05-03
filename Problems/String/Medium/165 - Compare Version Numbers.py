class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = j = 0
        res1 = version1.split('.')
        res2 = version2.split('.')

        for i in range(max(len(res1), len(res2))):
            n1  = 0 if i >= len(res1) else int(res1[i])
            n2  = 0 if i >= len(res2) else int(res2[i])

            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        
        return 0