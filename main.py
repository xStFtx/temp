class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()  # Sort for efficient processing
        moves = 0
        previous_num = -1  # Start with a value lower than all possible numbers
        
        for num in nums:
            if num <= previous_num:  
                moves += previous_num + 1 - num  # Calculate moves to make it unique
                previous_num += 1  # Update the 'target' value for the next number
            else:
                previous_num = num  # No moves needed, update the previous number
        
        return moves 
