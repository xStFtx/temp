from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # Initialize DP table with -1 to denote unvisited states.
        dp = [[[-1 for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]

        def dfs(row, col1, col2):
            # Check for out of bounds.
            if col1 < 0 or col1 >= cols or col2 < 0 or col2 >= cols:
                return 0
            
            # Check if the state has already been computed.
            if dp[row][col1][col2] != -1:
                return dp[row][col1][col2]
            
            # Calculate cherries picked by both robots at current positions.
            result = grid[row][col1] + (grid[row][col2] if col1 != col2 else 0)
            
            # If not at the last row, explore all possible moves for both robots.
            if row < rows - 1:
                max_cherries = 0
                for new_col1 in [col1 - 1, col1, col1 + 1]:
                    for new_col2 in [col2 - 1, col2, col2 + 1]:
                        max_cherries = max(max_cherries, dfs(row + 1, new_col1, new_col2))
                result += max_cherries
            
            dp[row][col1][col2] = result
            return result
        
        # Start DFS from the top row with both robots at the corners.
        return dfs(0, 0, cols - 1)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
    print(solution.cherryPickup(grid))  # Expected output: 24
