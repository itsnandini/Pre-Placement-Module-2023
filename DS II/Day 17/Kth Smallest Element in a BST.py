class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node, arr):
            if node is None:
                return arr
            arr = inorder(node.left, arr)
            arr.append(node.val)
            arr = inorder(node.right, arr)
            return arr
        
        arr = inorder(root, [])
        return arr[k-1]
