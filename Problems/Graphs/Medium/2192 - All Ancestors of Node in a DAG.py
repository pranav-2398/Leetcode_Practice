from typing import List

## REVERSE BFS ##################################################################
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Initialize adjacency list for the graph
        adjacency_list = [[] for _ in range(n)]

        # Populate the adjacency list with reversed edges
        for edge in edges:
            from_node, to_node = edge
            adjacency_list[to_node].append(from_node)

        def findChildren(node, visited):
            visited.add(node)

            for anc in adjacency_list[node]:
                if anc not in visited:
                    findChildren(anc, visited)

        res = []

        for i in range(n):
            ancestors = []
            visited = set()

            findChildren(i, visited)

            for node in range(n):
                if node == i:
                    continue
                if node in visited:
                    ancestors.append(node)
            
            res.append(ancestors)
        
        return res
    
## TOPOLOGICAL SORT ######################################################################
class Solution:
    def getAncestors(self, n, edges):
        # Create adjacency list
        adjacency_list = [[] for _ in range(n)]

        # Fill the adjacency list and indegree array based on the edges
        indegree = [0 for _ in range(n)]
        for edge in edges:
            from_node = edge[0]
            to = edge[1]
            adjacency_list[from_node].append(to)
            indegree[to] += 1

        # Queue for nodes with no incoming edges (starting points for topological sort)
        nodes_with_zero_indegree = [i for i in range(n) if indegree[i] == 0]

        # List to store the topological order of nodes
        topological_order = []
        while nodes_with_zero_indegree:
            current_node = nodes_with_zero_indegree.pop(0)
            topological_order.append(current_node)

            # Reduce indegree of neighboring nodes and add them to the queue
            # if they have no more incoming edges
            for neighbor in adjacency_list[current_node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    nodes_with_zero_indegree.append(neighbor)

        # Initialize the result list and set list for storing ancestors
        ancestors_list = [[] for _ in range(n)]
        ancestors_set_list = [set() for _ in range(n)]

        # Fill the set list with ancestors using the topological order
        for node in topological_order:
            for neighbor in adjacency_list[node]:
                # Add immediate parent, and other ancestors.
                ancestors_set_list[neighbor].add(node)
                ancestors_set_list[neighbor].update(ancestors_set_list[node])

        # Convert sets to lists and sort them
        for i in range(n):
            ancestors_list[i].extend(ancestors_set_list[i])
            ancestors_list[i].sort()

        return ancestors_list

s = Solution()
edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
n = 8
s.getAncestors(8, edges)