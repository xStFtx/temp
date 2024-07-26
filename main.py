class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Set the distance to self as 0
        for i in range(n):
            dist[i][i] = 0
        
        # Initialize the distances based on the given edges
        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w
        
        # Floyd-Warshall algorithm to find shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        min_reachable = float('inf')
        result_city = -1
        
        # Count reachable cities for each city
        for i in range(n):
            reachable = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            
            # Update result if this city has fewer or equal reachable cities
            if reachable <= min_reachable:
                min_reachable = reachable
                result_city = i
        
        return result_city