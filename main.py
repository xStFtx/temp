from collections import defaultdict
import heapq

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize the priority queue and visited set
        pq = [(0, 1)]  # (time, node)
        visited = set()
        times = [float('inf')] * (n + 1)
        times[1] = 0
        
        while pq:
            curr_time, node = heapq.heappop(pq)
            
            # If we've reached the target node for the second time
            if node == n and curr_time > times[n]:
                return curr_time
            
            # If we've visited this node twice with different times, continue
            if (node, curr_time) in visited:
                continue
            visited.add((node, curr_time))
            
            # Calculate the waiting time at the current node
            if curr_time % (2 * change) >= change:
                wait_time = 2 * change - (curr_time % (2 * change))
            else:
                wait_time = 0
            
            # Explore neighbors
            for neighbor in graph[node]:
                next_time = curr_time + wait_time + time
                if next_time < times[neighbor] or (times[neighbor] < next_time < times[n]):
                    heapq.heappush(pq, (next_time, neighbor))
                    if next_time < times[neighbor]:
                        times[neighbor] = next_time
        
        return -1  # If no second minimum path is found