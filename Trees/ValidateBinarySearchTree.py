# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, min_num, max_num):
            if not node:
                return True
        
            if node.val <= min_num or node.val >= max_num:
                return False
            
            return helper(node.left, min_num, node.val) and helper(node.right, node.val, max_num)

        return helper(root, float('-inf'), float('inf'))
