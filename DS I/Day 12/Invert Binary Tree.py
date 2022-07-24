# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        else:
            stack = []
            stack.append(root)
            while stack != []:
                curr_node = stack.pop()
                if curr_node.left != None or curr_node.right != None:
                    temp = curr_node.left
                    curr_node.left = curr_node.right
                    curr_node.right = temp
                if curr_node.right != None:
                    stack.append(curr_node.right)
                if curr_node.left != None:
                    stack.append(curr_node.left)
            return root
