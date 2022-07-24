class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def helper(node, target):
            if not node:
                return False
            
            target -= node.val
            
            if (target == 0) and (not node.left) and (not node.right):
                return True
            
            return helper(node.left, target) or helper(node.right, target)
        
        if not root:
            return
        
        return helper(root, sum)
