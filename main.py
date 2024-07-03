from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        
        # Compute the minimum difference after at most three moves
        return min(
            nums[-1] - nums[3],  # Remove the first three smallest elements
            nums[-2] - nums[2],  # Remove the first two smallest and the last largest
            nums[-3] - nums[1],  # Remove the first smallest and the last two largest
            nums[-4] - nums[0]   # Remove the last three largest elements
        )
