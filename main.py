from typing import List
from collections import defaultdict

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(conditions):
            graph = defaultdict(list)
            in_degree = defaultdict(int)
            
            for above, below in conditions:
                graph[above].append(below)
                in_degree[below] += 1
            
            queue = [i for i in range(1, k + 1) if in_degree[i] == 0]
            result = []
            
            while queue:
                node = queue.pop(0)
                result.append(node)
                
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            return result if len(result) == k else []

        row_order = topological_sort(rowConditions)
        col_order = topological_sort(colConditions)
        
        if not row_order or not col_order:
            return []
        
        position = {num: (row_order.index(num), col_order.index(num)) for num in range(1, k + 1)}
        
        matrix = [[0] * k for _ in range(k)]
        for num, (i, j) in position.items():
            matrix[i][j] = num
        
        return matrix