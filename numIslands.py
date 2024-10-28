def numIslands(self,grid):
    if not grid:
        return 0
    
    # Dimensions of the grid
    rows , cols = len(grid) , len(grid[0])
    island_count = 0 

    # Helper Function to perform DFS

    def dfs(r,c):
    # Base case: if out of bounds or at water, return
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0" :
            return

        grid[r][c] = "0"

        # Perform DFS in all 4 directions (up, down, left, right)

        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                island_count += 1
                dfs(r,c)
    
    return island_count



"""

r < 0 Prevents accessing cells above the grid.
r >= rows	Prevents accessing cells below the grid.
c < 0	Prevents accessing cells to the left.
c >= cols	Prevents accessing cells to the right.
grid[r][c] == "0"	Skips processing as it's not part of an island.


"""