from typing import List

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Create two separate Union-Find structures for Alice and Bob
        uf_alice = UnionFind(n + 1)
        uf_bob = UnionFind(n + 1)
        
        edges_used = 0
        
        # Step 1: Add all type 3 edges (shared by both Alice and Bob)
        for type_, u, v in edges:
            if type_ == 3:
                if uf_alice.union(u, v):
                    uf_bob.union(u, v)
                    edges_used += 1
        
        # Step 2: Add all type 1 edges (Alice only)
        for type_, u, v in edges:
            if type_ == 1:
                if uf_alice.union(u, v):
                    edges_used += 1
        
        # Step 3: Add all type 2 edges (Bob only)
        for type_, u, v in edges:
            if type_ == 2:
                if uf_bob.union(u, v):
                    edges_used += 1
        
        # Check if both Alice and Bob can fully traverse the graph
        # They should be able to reach n nodes (considering 1-based indexing)
        if len(set(uf_alice.find(i) for i in range(1, n + 1))) != 1 or \
           len(set(uf_bob.find(i) for i in range(1, n + 1))) != 1:
            return -1
        
        # The maximum number of edges we can remove
        return len(edges) - edges_used
