class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0  # Track the total number of moves

        def dfs(node):
            if not node:
                return 0

            left_balance = dfs(node.left)
            right_balance = dfs(node.right)

            # Calculate the balance factor of the current node
            balance = node.val - 1 + left_balance + right_balance

            # Update total moves with the absolute balance of this node
            self.moves += abs(balance) 

            # Return the balance of this node for its parent to use
            return balance

        dfs(root)
        
