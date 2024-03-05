class Solution:
    def minimumLength(self, s: str) -> int:
        # Initialize two pointers
        left, right = 0, len(s) - 1

        # Move the pointers towards each other
        while left < right and s[left] == s[right]:
            char = s[left]

            # Move left pointer to the right until a different character is found
            while left <= right and s[left] == char:
                left += 1

            # Move right pointer to the left until a different character is found
            while left <= right and s[right] == char:
                right -= 1

        # Return the remaining length of the string
        return max(0, right - left + 1)