class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, current_subset):
            # Append a copy of the current subset to the results
            result.append(current_subset[:])
            # Iterate over the possible next elements
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                current_subset.append(nums[i])
                # Recurse with the next element
                backtrack(i + 1, current_subset)
                # Exclude nums[i] from the current subset
                current_subset.pop()
        
        result = []
        backtrack(0, [])
        return result
