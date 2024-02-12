from typing import List
import time
import tracemalloc

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[[0 for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]

        for col1 in range(cols):
            for col2 in range(cols):
                if col1 == col2:
                    dp[rows-1][col1][col2] = grid[rows-1][col1]
                else:
                    dp[rows-1][col1][col2] = grid[rows-1][col1] + grid[rows-1][col2]

        for row in range(rows-2, -1, -1):
            for col1 in range(cols):
                for col2 in range(cols):
                    max_cherries = 0
                    for new_col1 in [col1 + move for move in (-1, 0, 1) if 0 <= col1 + move < cols]:
                        for new_col2 in [col2 + move for move in (-1, 0, 1) if 0 <= col2 + move < cols]:
                            max_cherries = max(max_cherries, dp[row+1][new_col1][new_col2])
                    dp[row][col1][col2] = grid[row][col1] + (grid[row][col2] if col1 != col2 else 0) + max_cherries

        return dp[0][0][cols-1]

if __name__ == "__main__":
    solution = Solution()
    grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]

    # Start tracking time and memory usage.
    tracemalloc.start()
    start_time = time.time()

    # Run the method.
    result = solution.cherryPickup(grid)

    # Stop tracking time and memory, and calculate the used resources.
    execution_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Print results and performance metrics.
    print(f"Result: {result}")  # Expected output: 24
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f"Memory usage: Current = {current / 1024**2:.6f} MB, Peak = {peak / 1024**2:.6f} MB")
