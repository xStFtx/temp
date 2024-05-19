class Solution:
    def maximumValueSum(self, nums, k, edges):
        # Calculate the initial sum of all node values
        initial_sum = sum(nums)
        
        # Calculate potential gains
        potential_gains = [(num ^ k) - num for num in nums]
        
        # Sum positive gains
        max_gain_sum = sum(gain for gain in potential_gains if gain > 0)
        
        # The maximum possible sum is the initial sum plus the positive gains
        return initial_sum + max_gain_sum

# Example usage:
solution = Solution()
print(solution.maximumValueSum([1, 2, 1], 3, [[0, 1], [0, 2]]))  # Output: 6
print(solution.maximumValueSum([2, 3], 7, [[0, 1]]))  # Output: 9
print(solution.maximumValueSum([7, 7, 7, 7, 7, 7], 3, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]))  # Output: 42
