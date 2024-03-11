class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Create a dictionary to store the index of each character in the order string
        order_dict = {char: idx for idx, char in enumerate(order)}
        
        # Define a custom sorting key function based on the order_dict
        def custom_key(char):
            return order_dict.get(char, float('inf'))  # Use float('inf') as default for characters not in order
        
        # Sort the characters in s based on the custom sorting key
        sorted_s = sorted(s, key=custom_key)
        
        # Join the sorted characters to form the result string
        return ''.join(sorted_s)