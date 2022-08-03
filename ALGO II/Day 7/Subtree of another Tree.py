# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a or not b:
                return a == b
            if a.val != b.val:
                return False
            return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)

        if not root:
            return False

        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
