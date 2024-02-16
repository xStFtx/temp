from collections import Counter
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Step 1: Count occurrences of each element
        count_map = Counter(arr)

        # Step 2: Sort elements based on their occurrences
        sorted_elements = sorted(count_map.items(), key=lambda x: x[1])

        # Step 3: Iterate through sorted elements and remove until k is satisfied
        unique_count = len(sorted_elements)
        for _, count in sorted_elements:
            if k >= count:
                k -= count
                unique_count -= 1
            else:
                break

        # Step 4: Return the remaining unique elements after removal
        return unique_count
