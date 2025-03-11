class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        from collections import defaultdict

        count = defaultdict(int)
        res = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # When window contains at least one 'a', 'b', and 'c'
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                # All substrings starting from left to right are valid
                res += len(s) - right
                count[s[left]] -= 1
                left += 1

        return res
