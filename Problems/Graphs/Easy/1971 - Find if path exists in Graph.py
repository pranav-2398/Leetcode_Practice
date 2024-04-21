from typing import DefaultDict, List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        matrix = DefaultDict(list)
        for start, end in edges:
            matrix[start].append(end)
            matrix[end].append(start)

        visited = set()

        def dfs(node):
            if node == destination:
                return True
                
            visited.add(node)
            
            for n in matrix[node]:
                if n not in visited:
                    if dfs(n):
                        return True
            
            return False
        
        return dfs(source)

s = Solution()
n = 3
# edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
# source = 5
# destination = 9
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
print(s.validPath(n, edges, source, destination))