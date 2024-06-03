class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Initialize pointers for both strings
        i, j = 0, 0
        # Length of the strings
        n, m = len(s), len(t)
        
        # Iterate through both strings
        while i < n and j < m:
            # If characters match, move the pointer on t
            if s[i] == t[j]:
                j += 1
            # Always move the pointer on s
            i += 1
        
        # The number of characters left in t that weren't matched in s
        return m - j