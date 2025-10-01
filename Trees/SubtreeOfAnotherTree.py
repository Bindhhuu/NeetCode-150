from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def rs(p, q):
            if not p and not q:
                return True
            if not p or not q: 
                return False
            if p.val != q.val:
                return False
            return rs(p.left, q.left) and rs(p.right, q.right)

        def same_tree(root):
            if not root:
                return False
            if rs(root, subRoot): 
                return True
            return same_tree(root.left) or same_tree(root.right) 
        return same_tree(root)
