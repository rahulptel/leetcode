from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def get_neighbours(row, col):
            neighbours = []
            for d in directions:
                nr, nc = row + d[0], col + d[1]
                if 0 <= nr < n_rows and 0 <= nc < n_cols and (nr, nc) not in visited:
                    neighbours.append((nr, nc))

            return neighbours

        def search(row, col):    
            if (row, col) in visited:
                return
            else:
                visited.add((row, col))

            for neighbour in get_neighbours(row, col):
                if grid[neighbour[0]][neighbour[1]] == "1":
                    search(neighbour[0], neighbour[1])

            # queue = deque(get_neighbours(row, col))
            # while len(queue):
            #     neighbour = queue.pop()
            #     if neighbour in visited:
            #         continue

            #     visited.add(neighbour)
            #     if grid[neighbour[0]][neighbour[1]] == "1":
            #         for nn in get_neighbours(neighbour[0], neighbour[1]):
            #             queue.append(nn)
            
        n_rows, n_cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        n_connected = 0
        
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    n_connected += 1
                    search(row, col)


        return n_connected        
