from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        
        # Step 1: Calculate the minimum distance from each cell to the nearest thief
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        
        # Helper function to check if there's a path with at least `min_safeness` safeness factor
        def canReachEnd(min_safeness):
            if dist[0][0] < min_safeness:
                return False
            
            visited = [[False] * n for _ in range(n)]
            queue = deque([(0, 0)])
            visited[0][0] = True
            
            while queue:
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and dist[nr][nc] >= min_safeness:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            
            return False
        
        # Binary search for the maximum safeness factor
        left, right = 0, min(dist[0][0], dist[n-1][n-1])
        
        while left < right:
            mid = (left + right + 1) // 2
            if canReachEnd(mid):
                left = mid
            else:
                right = mid - 1
        
        return left

# Example usage
solution = Solution()
grid = [[0,0,1],[0,0,0],[0,0,0]]
print(solution.maximumSafenessFactor(grid))  # Output: 2
