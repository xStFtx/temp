class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search_root(self, word):
        node = self.root
        prefix = ""
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            prefix += char
            if node.is_end_of_word:
                return prefix
        return word
    
    def replaceWords(self, dictionary, sentence):
        # Build the Trie
        for root in dictionary:
            self.insert(root)
        
        # Replace words in the sentence
        words = sentence.split()
        replaced_words = [self.search_root(word) for word in words]
        
        # Reconstruct the sentence
        return ' '.join(replaced_words)

