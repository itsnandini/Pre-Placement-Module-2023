from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        get_val = lambda item: item.val if item else None
        q = deque()
        
        if not root:
            return str([])
        else:
            res = [root.val]
            q.append(root)
        while q:
            l=[]
            len_q = len(q)
            for i in range(len_q):
                item = q.popleft()
                if item and item.left:
                    q.append(item.left)
                if item and item.right:
                    q.append(item.right)
                l.append(get_val(item.left))
                l.append(get_val(item.right))
            if not all(x is None for x in l):
                res += l
        ind =len(res)
        for i in res[::-1]:
            if i is not None:break
            else:ind-=1
        return str(res[:ind])
                     
    def deserialize(self, data):
        if len(data)==0 or data=='[]':
            return []
        de_data = data[1:-1].split(', ')
        return [int(d) if d!='None' else None for d in de_data]
