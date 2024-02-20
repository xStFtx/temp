class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        missing_number = n
        
        for i in range(n):
            missing_number ^= i ^ nums[i]
        
        return missing_number
