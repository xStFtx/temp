from collections import deque

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            # Maintain max_deque for the maximum element in the current window
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain min_deque for the minimum element in the current window
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Check if the current window is valid
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                # Move left pointer to make the window valid again
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Update the maximum length of the valid subarray
            max_len = max(max_len, right - left + 1)
        
        return max_len
