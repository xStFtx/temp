# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.total = 0  # to keep track of the running sum
        
        def reverse_inorder(node: TreeNode):
            if not node:
                return
            # Traverse the right subtree first
            reverse_inorder(node.right)
            # Update the node's value with the running sum
            self.total += node.val
            node.val = self.total
            # Traverse the left subtree
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root
