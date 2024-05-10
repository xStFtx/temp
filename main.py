import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        pq = [(-arr[0] / arr[n - 1], 0, n - 1)]
        
        for _ in range(k - 1):
            neg_frac, i, j = heapq.heappop(pq)
            if i + 1 < j:
                heapq.heappush(pq, (-arr[i + 1] / arr[j], i + 1, j))
        
        neg_frac, i, j = heapq.heappop(pq)
        return [arr[i], arr[j]]