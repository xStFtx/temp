class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def get_mapped_value(num: int) -> int:
            if num == 0:
                return mapping[0]
            
            mapped = 0
            multiplier = 1
            while num > 0:
                digit = num % 10
                mapped += mapping[digit] * multiplier
                multiplier *= 10
                num //= 10
            return mapped
        
        indexed_nums = [(i, num, get_mapped_value(num)) for i, num in enumerate(nums)]
        indexed_nums.sort(key=lambda x: (x[2], x[0]))
        
        return [num for _, num, _ in indexed_nums]