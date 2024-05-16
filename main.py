# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            # Leaf node: return its boolean value
            return root.val == 1
        
        # Non-leaf node: evaluate left and right children
        left_value = self.evaluateTree(root.left)
        right_value = self.evaluateTree(root.right)
        
        if root.val == 2:
            # OR operation
            return left_value or right_value
        elif root.val == 3:
            # AND operation
            return left_value and right_value

# Example usage:
# Construct the tree [2, 1, 3, null, null, 0, 1]
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

solution = Solution()
print(solution.evaluateTree(root))  # Output: True
