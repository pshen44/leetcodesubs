# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = 0
        def search(node, res, target) -> bool:
            if not node:
                return False
            res += node.val
            if not node.left and not node.right:
                return res == target

            return (search(node.left, res, target) or search(node.right, res, target))
        return search(root, res, targetSum)

