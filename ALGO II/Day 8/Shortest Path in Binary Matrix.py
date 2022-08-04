class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)-1
        if grid[0][0] or grid[n][n]: return -1
        q, grid[0][0] = [0], 1
        while len(q):
            curr = q.pop(0)
            i, j = curr & ((1 << 7) - 1), curr >> 7
            if i == n and j == n: return grid[n][n]
            for a in range(max(i-1,0),min(i+2,n+1)):
                for b in range(max(j-1,0),min(j+2,n+1)):
                    if grid[a][b] == 0:
                        grid[a][b] = grid[i][j] + 1
                        q.append(a + (b << 7))
        return -1
