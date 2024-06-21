from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        # Calculate the initial satisfied customers without using the technique
        satisfied_customers = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        
        # Calculate the potential increase in satisfied customers by applying the technique
        # Initialize the extra satisfied customers in the first window of 'minutes'
        extra_satisfied = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        max_extra_satisfied = extra_satisfied
        
        # Sliding window to calculate the extra satisfied customers for each possible window
        for i in range(minutes, n):
            if grumpy[i] == 1:
                extra_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                extra_satisfied -= customers[i - minutes]
            max_extra_satisfied = max(max_extra_satisfied, extra_satisfied)
        
        # Total satisfied customers is the initially satisfied plus the maximum extra satisfied
        return satisfied_customers + max_extra_satisfied

