from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[[None for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]
        
        def dfs(row, col1, col2):
            if col1 < 0 or col1 >= cols or col2 < 0 or col2 >= cols:
                return 0
            if dp[row][col1][col2] is not None:
                return dp[row][col1][col2]
            result = grid[row][col1] + (grid[row][col2] if col1 != col2 else 0)
            if row != rows - 1:
                max_cherries = 0
                for new_col1 in [col1-1, col1, col1+1]:
                    for new_col2 in [col2-1, col2, col2+1]:
                        max_cherries = max(max_cherries, dfs(row + 1, new_col1, new_col2))
                result += max_cherries
            dp[row][col1][col2] = result
            return result
        
        return dfs(0, 0, cols-1)
