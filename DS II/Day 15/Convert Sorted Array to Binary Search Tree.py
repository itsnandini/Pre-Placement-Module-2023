# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n == 0: return None
        
        return self.arr2bst_helper(nums, 0, n-1, n)
        
    def arr2bst_helper(self, nums, lo, hi, n):
        if lo > hi: return None
        
        mid = (lo+hi)//2
        node = TreeNode(nums[mid])
        if lo == hi:
            return node
        
        node.left = self.arr2bst_helper(nums, lo, mid-1, n)
        node.right = self.arr2bst_helper(nums, mid+1, hi, n)
        
        return node
