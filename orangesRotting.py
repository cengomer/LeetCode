from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        if not grid:
            return -1

        # Direction vectors to check 4 directions (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        fresh_oranges = 0
        time = 0

        # First, find all rotten oranges and count fresh oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))  # Add all rotten oranges to the queue
                elif grid[r][c] == 1:
                    fresh_oranges += 1  # Count fresh oranges

        # If there are no fresh oranges, return 0 (nothing needs to rot)
        if fresh_oranges == 0:
            return 0

        # BFS to rot the fresh oranges
        while queue:
            for i in range(len(queue)):  # Process one level of BFS
                r, c = queue.popleft()

                # Explore 4-directionally adjacent cells
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc

                    # Check if the new cell is within bounds and has a fresh orange
                    if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 1:
                        # Rot the fresh orange
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c))  # Add it to the queue
                        fresh_oranges -= 1  # Decrease the count of fresh oranges

            # After processing all oranges at the current time level, increment time
            time += 1

        # If there are still fresh oranges, return -1, else return time - 1
        return time - 1 if fresh_oranges == 0 else -1
