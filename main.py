class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Function to swap elements in the array
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        # Place each number in its correct position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                swap(nums, i, nums[i] - 1)
        
        # Iterate through the array to find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positive integers are present, return n + 1
        return n + 1
