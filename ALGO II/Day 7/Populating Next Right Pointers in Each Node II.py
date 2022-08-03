"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        ans=[]
        def dfs(node,level):
            if not(node):
                return
            if level==len(ans):
                ans.append([])
            if not(ans[level]):
                ans[level].append(node)
            else:
                ans[level][-1].next=node
                ans[level].append(node)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        return root
