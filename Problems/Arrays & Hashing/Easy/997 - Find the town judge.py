class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return n 
            
        t1 = Counter([x for x,y in trust])
        t2 = Counter([y for x,y in trust])

        for k in t2.keys():
            if not t1.get(k) and t2[k] == n-1:
                return k
        
        return -1