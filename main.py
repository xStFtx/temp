import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(len(quality))])
        heap = [-q for q in workers[:k][1]]
        heapq.heapify(heap)
        total_quality = sum([-q for q in heap])
        min_cost = float('inf')

        for ratio, q in workers:
            total_quality += q
            heapq.heappush(heap, -q)
            if len(heap) > k:
                total_quality += heapq.heappop(heap)
            min_cost = min(min_cost, total_quality * ratio)

        return min_cost