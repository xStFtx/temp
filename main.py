from typing import List
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair_all(time: int) -> bool:
            total_cars = 0
            for rank in ranks:
                total_cars += int(math.isqrt(time // rank))  # floor(sqrt(time / rank))
            return total_cars >= cars

        left, right = 1, min(ranks) * cars * cars  # upper bound of time
        
        result = right
        while left <= right:
            mid = (left + right) // 2
            if can_repair_all(mid):
                result = mid
                right = mid - 1  # try to find smaller feasible time
            else:
                left = mid + 1  # need more time
        
        return result
