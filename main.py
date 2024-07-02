from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Step 1: Count the frequency of elements in both arrays
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        # Step 2: Find the intersection
        intersection = []
        for num in count1:
            if num in count2:
                # Step 3: Determine the minimum count for the common element
                min_count = min(count1[num], count2[num])
                # Add the element min_count times to the intersection list
                intersection.extend([num] * min_count)
        
        return intersection

