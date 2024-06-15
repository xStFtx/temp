from heapq import heappop, heappush

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        # Min heap for capital, max heap for profits
        min_capital_heap = []
        max_profit_heap = []
        
        # Populate the min heap with projects sorted by their capital requirements
        for c, p in zip(capital, profits):
            heappush(min_capital_heap, (c, p))
        
        # Iterate k times or until no more projects can be completed
        for _ in range(k):
            # Move all projects that can be started with current capital to the max profit heap
            while min_capital_heap and min_capital_heap[0][0] <= w:
                c, p = heappop(min_capital_heap)
                heappush(max_profit_heap, -p)  # use negative to simulate max heap
            
            # If no projects can be started, break the loop
            if not max_profit_heap:
                break
            
            # Select the project with the maximum profit
            w += -heappop(max_profit_heap)
        
        return w
