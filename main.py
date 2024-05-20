class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        subset_count = 1 << n  # 2^n
        
        for i in range(subset_count):
            subset_xor = 0
            for j in range(n):
                if i & (1 << j):
                    subset_xor ^= nums[j]
            total_sum += subset_xor
        
        return total_sum
