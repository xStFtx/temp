from typing import List
from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Step 1: Create the graph and compute in-degrees
        graph = defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        # Step 2: Perform topological sort using Kahn's algorithm
        topo_order = []
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 3: Collect ancestors using the topological order
        ancestors = [set() for _ in range(n)]
        
        for node in topo_order:
            for neighbor in graph[node]:
                # Add current node to the ancestor list of the neighbor
                ancestors[neighbor].add(node)
                # Add all ancestors of the current node to the ancestor list of the neighbor
                ancestors[neighbor].update(ancestors[node])
        
        # Convert sets to sorted lists
        result = [sorted(list(anc)) for anc in ancestors]
        
        return result
