class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Create the expected array by sorting the heights array
        expected = sorted(heights)
        
        # Count the number of indices where heights and expected do not match
        mismatch_count = sum(1 for i in range(len(heights)) if heights[i] != expected[i])
        
        return mismatch_count
