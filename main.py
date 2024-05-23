class Solution:
    def beautifulSubsets(self, nums, k):
        from collections import Counter
        
        def backtrack(index, count_map):
            if index == len(nums):
                # If there is at least one element in the subset, it's a valid subset
                return 1 if count_map else 0
            
            count = 0
            # Case 1: Exclude the current element
            count += backtrack(index + 1, count_map)
            
            # Case 2: Include the current element, only if it does not violate the beautiful subset condition
            current_num = nums[index]
            if count_map[current_num - k] == 0 and count_map[current_num + k] == 0:
                count_map[current_num] += 1
                count += backtrack(index + 1, count_map)
                count_map[current_num] -= 1
            
            return count
        
        # Frequency map to keep track of the elements in the current subset
        count_map = Counter()
        # Start backtracking from index 0
        return backtrack(0, count_map)