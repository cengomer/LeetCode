class Solution(object):
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                return 0

            grid[r][c] = 0  # Mark as visited
            area = 1  # Current cell

            # Explore all four directions and accumulate the area
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    current_area = dfs(r, c)
                    max_area = max(max_area, current_area)

        return max_area
