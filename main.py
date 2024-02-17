import heapq
from typing import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        diff_heap = []  # Min heap to store the differences between consecutive buildings' heights

        for i in range(1, n):
            diff = heights[i] - heights[i - 1]

            if diff > 0:
                heapq.heappush(diff_heap, diff)

                # If the number of differences exceeds the available ladders, use bricks
                if len(diff_heap) > ladders:
                    bricks -= heapq.heappop(diff_heap)

                # If there are not enough bricks, return the current index
                if bricks < 0:
                    return i - 1

        return n - 1
