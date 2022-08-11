class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = [root]
        res = []
        while q:
            n = len(q)
            for i in range(n):
                popped = q.pop(0)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                if i == n - 1:
                    res.append(popped.val)
        return res
