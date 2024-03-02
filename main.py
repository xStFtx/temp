from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Square each element in the array
        squares = [num ** 2 for num in nums]
        
        # Sort the squared array
        squares.sort()
        
        return squares
