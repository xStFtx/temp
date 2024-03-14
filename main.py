class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        prefix_sum = {0: 1}  # Initializing with {0: 1} to handle edge cases
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num
            target = curr_sum - goal

            if target in prefix_sum:
                count += prefix_sum[target]

            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        return count