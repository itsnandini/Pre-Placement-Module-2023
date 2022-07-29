class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        total = n*n
        for i in range(1,total+1):
            matrix.append(i)
        result = [[None]*n for _ in range(n)]
        
        for d in range(n-1):
            for i in range(d, n-d-1):
                result[d][i]=matrix.pop(0)
            for i in range(d, n-d-1):
                result[i][n-d-1]=matrix.pop(0)
            for i in range(n-d-1,d,-1):
                result[n-d-1][i]=matrix.pop(0)
            for i in range(n-d-1,d,-1):
                result[i][d]=matrix.pop(0)
        if n%2:
            x= (n-1)//2
            result[x][x]=matrix.pop()
        return result
