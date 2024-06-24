from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_count = 0
        queue = deque()  # to track the flip operations
        
        for i in range(n):
            # Remove indices from the queue that are out of the window of size k
            if queue and queue[0] + k <= i:
                queue.popleft()
            
            # If the current element is 0 and the number of flips affecting it is even, we need to flip
            if len(queue) % 2 == nums[i]:
                # If we can't flip a k-length subarray from index i, return -1
                if i + k > n:
                    return -1
                # Perform a flip, add the starting index of the flip to the queue
                queue.append(i)
                flip_count += 1
        
        return flip_count
