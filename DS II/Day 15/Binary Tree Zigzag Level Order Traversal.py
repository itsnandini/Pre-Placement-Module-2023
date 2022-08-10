# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        to_right = 1
        
        if root == None:
            return []
        
        cur_queue = [root]
        next_queue = []
        result = []
        tmp = []
        while(cur_queue):
            
            node = cur_queue.pop()
            tmp.append(node.val)
            if(to_right):
                if(node.left):
                    next_queue.append(node.left)
                if(node.right):
                    next_queue.append(node.right)
            else:
                if(node.right):
                    next_queue.append(node.right)
                if(node.left):
                    next_queue.append(node.left)
            
            if(not cur_queue):
                cur_queue = next_queue
                next_queue = []
                to_right = not to_right
                result.append(tmp)
                tmp = []
        
        return result
