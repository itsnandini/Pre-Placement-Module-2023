class CircleNumFinder:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        num = 0
        def dfs(start):
            for k in range(len(isConnected[start])):
                if isConnected[start][k] == 1 and k not in visited:
                    visited.add(k)
                    dfs(k)
                
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
                    num += 1
        return num
