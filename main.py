class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all elements to get the XOR of the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Find a bit that is set in xor_all (we can use the rightmost set bit)
        differentiating_bit = xor_all & -xor_all
        
        # Step 3: Partition the array into two groups and XOR within each group
        num1 = 0
        num2 = 0
        for num in nums:
            if num & differentiating_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        # Step 4: The two unique numbers are num1 and num2
        return [num1, num2]

