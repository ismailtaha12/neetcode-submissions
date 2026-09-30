from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(row, col):
            queue = deque([(row, col)])
            visited.add((row, col))

            while queue:
                row, col = queue.popleft()

                neighbors = [
                    (row + 1, col),
                    (row - 1, col),
                    (row, col + 1),
                    (row, col - 1)
                ]

                for next_row, next_col in neighbors:
                    if next_row < 0 or next_row >= rows:
                        continue
                    if next_col < 0 or next_col >= cols:
                        continue

                    if grid[next_row][next_col] == "0":
                        continue
                    if (next_row, next_col) in visited:
                        continue

                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col))

        islands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    if (row, col) not in visited:
                        islands += 1
                        bfs(row, col)

        return islands