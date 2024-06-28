from typing import List
from collections import defaultdict

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Count the degree of each city
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        
        # Step 2: Sort cities by their degree
        city_degree = sorted(range(n), key=lambda x: degree[x], reverse=True)
        
        # Step 3: Assign the values from n to 1 based on sorted degrees
        value_assignment = [0] * n
        for i, city in enumerate(city_degree):
            value_assignment[city] = n - i
        
        # Step 4: Calculate the total importance of all roads
        total_importance = 0
        for a, b in roads:
            total_importance += value_assignment[a] + value_assignment[b]
        
        return total_importance

