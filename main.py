from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive_odds = 0  # Counter for consecutive odd numbers
        
        for num in arr:
            if num % 2 == 1:
                consecutive_odds += 1
                if consecutive_odds == 3:
                    return True
            else:
                consecutive_odds = 0
        
        return False
