from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        def bfs(node):
            if node:
                queue.append(node)
            while len(queue) > 0:
                layer = []
                for i in range(len(queue)):
                    n = queue.popleft()
                    layer.append(n.val)
                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)
                res.append(layer)
        bfs(root)
        return res


