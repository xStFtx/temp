from collections import Counter
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Count the frequency of each element
        freq_counter = Counter(nums)

        # Find the maximum frequency
        max_freq = max(freq_counter.values())

        # Count the number of elements with maximum frequency
        max_freq_count = sum(1 for freq in freq_counter.values() if freq == max_freq)

        return max_freq_count