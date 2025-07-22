# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pRes = []
        qRes = []
        def inorder(node, result):
            res = []
            if not node:
                res.append(None)
                return node
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)
            result.append(res)
        inorder(p, pRes)
        inorder(q, qRes)
        print(pRes, qRes)
        if pRes == qRes:
            return True
        else:
            return False

