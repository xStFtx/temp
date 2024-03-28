class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency = {}
        max_length = 0
        left = 0
        
        for right, num in enumerate(nums):
            frequency[num] = frequency.get(num, 0) + 1
            
            while max(frequency.values()) > k:
                frequency[nums[left]] -= 1
                left += 1
                
            max_length = max(max_length, right - left + 1)
        
        return max_length
