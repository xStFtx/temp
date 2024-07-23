from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number
        freq = Counter(nums)
        
        # Create a list of tuples (num, frequency)
        num_freq = [(num, freq[num]) for num in nums]
        
        # Sort the list based on frequency (ascending) and value (descending)
        num_freq.sort(key=lambda x: (x[1], -x[0]))
        
        # Return the sorted list of numbers
        return [num for num, _ in num_freq]