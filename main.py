from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        level = 0  # Level index

        while queue:
            size = len(queue)
            prev_value = float('-inf') if level % 2 == 0 else float('inf')

            for _ in range(size):
                node = queue.popleft()

                # Check the value at the current level
                if (level % 2 == 0 and (node.val % 2 == 0 or node.val <= prev_value)) or \
                   (level % 2 == 1 and (node.val % 2 == 1 or node.val >= prev_value)):
                    return False

                prev_value = node.val

                # Add children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return True
