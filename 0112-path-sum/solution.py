# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backtrack(node, total):
            if not node:
                return False
            total += node.val
            if not node.right and not node.left:
                return total == targetSum
            return backtrack(node.right, total) or backtrack(node.left, total)
            
        return backtrack(root, 0)
