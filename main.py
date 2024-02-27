# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # Diameter at each node is the sum of depths of left and right subtrees
            self.result = max(self.result, left_depth + right_depth)
            # Return the depth of the current node
            return 1 + max(left_depth, right_depth)

        self.result = 0  # Variable to store the diameter
        depth(root)
        return self.result
