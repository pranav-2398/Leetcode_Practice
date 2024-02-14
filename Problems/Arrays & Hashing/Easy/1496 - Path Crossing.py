class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coordinates = {(0,0):0}
        start_point = (0,0)

        for p in path:
            if p == 'N':
                start_point = tuple(map(lambda i, j: i + j, start_point, (0, 1)))
            
            elif p == 'E':
                start_point = tuple(map(lambda i, j: i + j, start_point, (1, 0)))

            elif p == 'W':
                start_point = tuple(map(lambda i, j: i + j, start_point, (-1, 0)))

            else:
                start_point = tuple(map(lambda i, j: i + j, start_point, (0, -1)))
                
            if start_point in coordinates:
                return True
            else:
                coordinates[start_point] = 0

        return False

soln = Solution()

print(soln.isPathCrossing('NESWW'))
            