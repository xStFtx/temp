class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Dictionary to store cumulative sum % k and its index
        mod_sum_index = {0: -1}
        cum_sum = 0
        
        for i, num in enumerate(nums):
            cum_sum += num
            if k != 0:
                cum_sum %= k
            
            if cum_sum in mod_sum_index:
                if i - mod_sum_index[cum_sum] >= 2:
                    return True
            else:
                mod_sum_index[cum_sum] = i
        
        return False