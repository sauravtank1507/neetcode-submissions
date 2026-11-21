class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def numIsland(grid):
            rows, cols = len(grid), len(grid[0])
            count = 0

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == '1':
                        count += 1
                        markIsland(grid, r, c, rows, cols)

            return count

        def markIsland(grid, r, c, rows, cols):
            if (r < 0 or r >= rows) or (c < 0 or c >= cols) or (grid[r][c] != '1'):

                return

            grid[r][c] = '0'

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                markIsland(grid, r + dr, c + dc, rows, cols)

        return numIsland(grid)