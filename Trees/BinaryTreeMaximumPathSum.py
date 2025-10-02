# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxx = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            leftt = max(dfs(node.left), 0)
            rightt = max(dfs(node.right), 0)
            path = node.val + leftt + rightt

            self.maxx = max(self.maxx, path)

            return node.val + max(leftt, rightt)

        dfs(root)
        return self.maxx
