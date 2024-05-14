class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_gold = 0

        def dfs(row, col, gold):
            nonlocal max_gold
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return 0

            gold += grid[row][col]
            max_gold = max(max_gold, gold)
            temp = grid[row][col]
            grid[row][col] = 0  # Mark as visited

            # Explore all neighbors
            dfs(row - 1, col, gold)  # Up
            dfs(row + 1, col, gold)  # Down
            dfs(row, col - 1, gold)  # Left
            dfs(row, col + 1, gold)  # Right

            grid[row][col] = temp  # Reset the value

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    dfs(i, j, 0)

        return max_gold