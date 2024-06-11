from collections import Counter

class Solution:
    def relativeSortArray(self, arr1, arr2):
        # Step 1: Count the occurrences of each element in arr1
        count = Counter(arr1)
        
        # Step 2: Arrange elements according to arr2
        result = []
        for num in arr2:
            if num in count:
                result.extend([num] * count[num])
                del count[num]
        
        # Step 3: Append the remaining elements sorted in ascending order
        remaining = []
        for num in count:
            remaining.extend([num] * count[num])
        
        result.extend(sorted(remaining))
        
        return result

