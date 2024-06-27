from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # We only need to check the first two edges to find the common node
        # Because the center node will appear in both of these edges
        a, b = edges[0]
        c, d = edges[1]
        
        # The center node will be the common node between the first two edges
        if a == c or a == d:
            return a
        return b
