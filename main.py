class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_counts = {0: 1}  # Base case: empty subarray (sum 0) has remainder 0
        cumsum = 0
        result = 0

        for num in nums:
            cumsum = (cumsum + num) % k  # Calculate cumulative sum modulo k
            result += remainder_counts.get(cumsum, 0)  # Add count of previous subarrays with same remainder
            remainder_counts[cumsum] = remainder_counts.get(cumsum, 0) + 1  # Update count for current remainder

        return result
