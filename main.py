from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Find first index of number >= 0
        neg_count = bisect_left(nums, 0)
        
        # Find first index of number > 0
        pos_start = bisect_right(nums, 0)
        pos_count = len(nums) - pos_start
        
        # Return max of both counts
        return max(neg_count, pos_count)
