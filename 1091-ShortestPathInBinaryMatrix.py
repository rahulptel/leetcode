from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        GRID_SIZE = len(grid)
        q = deque([(0, 0, 1)])
        visited = set((0, 0))
        
        # iterate while q is not empty
        while len(q):
            x, y, dist = q.popleft()
            if x == GRID_SIZE-1 and y == GRID_SIZE-1:
                return dist

            for i in range(max(0, x-1), min(x+2, GRID_SIZE)):
                for j in range(max(0, y-1), min(y+2, GRID_SIZE)):
                    if (i, j) not in visited and grid[i][j] == 0:                    
                        q.append((i, j, dist+1))
                        visited.add((i, j))

        return -1

        
