from typing import List
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Convert nums array to a binary array indicating odd (1) and even (0) numbers
        odd_indicator = [1 if num % 2 != 0 else 0 for num in nums]
        
        prefix_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # To account for subarrays starting from index 0
        result = 0
        
        for odd in odd_indicator:
            prefix_sum += odd
            # If there is a previous prefix sum that equals to prefix_sum - k, add its count to result
            if prefix_sum - k in prefix_counts:
                result += prefix_counts[prefix_sum - k]
            # Increment the count of the current prefix sum in the hashmap
            prefix_counts[prefix_sum] += 1
        
        return result