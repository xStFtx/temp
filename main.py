from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize pointers for both arrays
        i, j = 0, 0
        
        # Iterate until one of the arrays is exhausted
        while i < len(nums1) and j < len(nums2):
            # If the current elements are equal, return the common element
            if nums1[i] == nums2[j]:
                return nums1[i]
            
            # Move the pointer for the smaller element
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        # No common element found
        return -1