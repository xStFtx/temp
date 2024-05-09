from heapq import heappush, heappop

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n = len(happiness)
        happiness.sort(reverse=True)  # Sort the happiness values in descending order
        max_heap = [-val for val in happiness]  # Initialize a max-heap with negated values
        heapq.heapify(max_heap)

        total_happiness = 0
        for _ in range(k):
            current_max = -heappop(max_heap)  # Get the maximum remaining happiness value
            total_happiness += current_max
            if max_heap:
                heappush(max_heap, current_max - 1)  # Decrement the happiness values of the remaining children

        return total_happiness