class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count the frequency of each character
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Initialize the length of the longest palindrome
        longest_palindrome_length = 0
        
        # Flag to check if there is any character with odd frequency
        odd_exists = False
        
        # Iterate through the character counts
        for count in char_count.values():
            if count % 2 == 0:
                longest_palindrome_length += count
            else:
                longest_palindrome_length += count - 1
                odd_exists = True
        
        # If there was any character with odd frequency, add one to the length
        if odd_exists:
            longest_palindrome_length += 1
        
        return longest_palindrome_length
