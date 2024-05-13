class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Step 1: Maximize leading 1's for each row
        for row in grid:
            if row[0] == 0:
                for j in range(n):
                    row[j] = 1 - row[j]
        
        # Step 2: Maximize the number of 1's for each column
        for j in range(1, n):
            col_sum = sum(row[j] for row in grid)
            if col_sum < m / 2:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]
        
        # Step 3: Compute the score
        score = 0
        for row in grid:
            binary_str = ''.join(str(x) for x in row)
            score += int(binary_str, 2)
        
        return score