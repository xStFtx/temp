import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        heap = [(0, src, 0)]  # (cost, current city, stops)
        memo = {}

        while heap:
            cost, current, stops = heapq.heappop(heap)

            if current == dst:
                return cost

            if stops <= k:
                if (current, stops) not in memo or cost < memo[(current, stops)]:
                    memo[(current, stops)] = cost
                    for neighbor, price in graph[current]:
                        heapq.heappush(heap, (cost + price, neighbor, stops + 1))

        return -1
