class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[]
        for i in range(1,n+1,1):
            nums.append(i)
        temp=[]
        result=[]
        def dfs(m,num):
            if m==k:
                result.append(temp[:])
                return
            else:
                if len(num)<k-m:
                    return
                for i in range(len(num)):
                    temp.append(num[i])
                    dfs(m+1,num[i+1:])
                    temp.pop()
        dfs(0,nums)
        return result
