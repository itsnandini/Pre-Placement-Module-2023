# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root:
            cur = root
            while 1:
                if cur.val<val:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = TreeNode(val)
                        break
                if cur.val>val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = TreeNode(val)
                        break
            return root
        else:
            return TreeNode(val)
