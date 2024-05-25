class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Convert the wordDict to a set for O(1) look-ups
        wordSet = set(wordDict)
        memo = {}  # Memoization dictionary
        
        def backtrack(sub_s):
            if sub_s in memo:
                return memo[sub_s]
            
            if not sub_s:
                return []
            
            res = []
            for end in range(1, len(sub_s) + 1):
                word = sub_s[:end]
                if word in wordSet:
                    if end == len(sub_s):
                        res.append(word)
                    else:
                        for sub_sentence in backtrack(sub_s[end:]):
                            res.append(word + ' ' + sub_sentence)
            
            memo[sub_s] = res
            return res
        
        return backtrack(s)
