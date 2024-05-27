class Solution:
    def specialArray(self, nums):
        # Sort the array
        nums.sort(reverse=True)
        
        # Check each possible value of x
        for x in range(1, len(nums) + 1):
            # Check if there are exactly x elements greater than or equal to x
            if nums[x-1] >= x and (x == len(nums) or nums[x] < x):
                return x
        
        return -1
