# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(root, top, bot):
            if not root:
                return True
            if not (bot < root.val < top):
                return False
            return (bst(root.right, top, root.val) and bst(root.left, root.val, bot))

        return bst(root, float("inf"), float("-inf"))

        
