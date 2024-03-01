class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Find the last occurrence of '1'
        last_one_index = s.rfind('1')
        
        # If there is only one '1', return the input string as is
        if last_one_index == 0:
            return s
        
        # If there are multiple '1's, move the last '1' to the end
        # and remove the original occurrence of '1'
        modified_s = s[:last_one_index] + s[last_one_index+1:] + '1'
        
        return modified_s

