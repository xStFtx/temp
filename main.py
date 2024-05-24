from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        from collections import Counter
        
        def word_score(word):
            return sum(score[ord(c) - ord('a')] for c in word)
        
        def can_form(word, letter_count):
            word_count = Counter(word)
            for char, cnt in word_count.items():
                if letter_count[char] < cnt:
                    return False
            return True
        
        def backtrack(index, letter_count, current_score):
            if index == len(words):
                return current_score
            
            # Skip current word
            max_score = backtrack(index + 1, letter_count, current_score)
            
            # Include current word if possible
            word = words[index]
            if can_form(word, letter_count):
                for char in word:
                    letter_count[char] -= 1
                max_score = max(max_score, backtrack(index + 1, letter_count, current_score + word_score(word)))
                for char in word:
                    letter_count[char] += 1
            
            return max_score
        
        letter_count = Counter(letters)
        return backtrack(0, letter_count, 0)

