from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Find the intersection using set operations
        intersection_set = set(nums1) & set(nums2)
        
        # Convert the set back to a list
        intersection_list = list(intersection_set)
        
        return intersection_list
