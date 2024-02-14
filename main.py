from typing import List
import time
import tracemalloc
from itertools import product

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp_current = [[0] * cols for _ in range(cols)]
        dp_next = [[0] * cols for _ in range(cols)]
        directions = (-1, 0, 1)

        memo = {}

        def valid_moves(col):
            return [col + move for move in directions if 0 <= col + move < cols]

        for row in range(rows - 1, -1, -1):
            for col1, col2 in product(range(cols), repeat=2):
                result = grid[row][col1] + (grid[row][col2] if col1 != col2 else 0)

                if row < rows - 1:
                    max_cherries = max(
                        dp_next[new_col1][new_col2]
                        for new_col1, new_col2 in product(
                            valid_moves(col1), valid_moves(col2)
                        )
                    )
                    result += max_cherries

                dp_current[col1][col2] = result

            dp_current, dp_next = dp_next, dp_current

        return dp_next[0][cols - 1]

if __name__ == "__main__":
    solution = Solution()
    grid = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]

    tracemalloc.start()
    start_time = time.time()

    result = solution.cherryPickup(grid)

    execution_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Result: {result}")  # Expected output: 24
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f"Memory usage: Current = {current / 1024**2:.6f} MB, Peak = {peak / 1024**2:.6f} MB")
