from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the counter with the first word
        common_count = Counter(words[0])
        
        # Iterate through the rest of the words
        for word in words[1:]:
            # Create a counter for the current word
            current_count = Counter(word)
            # Update the common count with the minimum frequency of each character
            for char in common_count:
                if char in current_count:
                    common_count[char] = min(common_count[char], current_count[char])
                else:
                    common_count[char] = 0
        
        # Collect the results
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result
