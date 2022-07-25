class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        n = len(triangle[-1])
        dp = [i for i in triangle[-1]]
    
        for i in range(m - 2, -1, -1):
            for j in range(len(triangle[i])):                
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        
        return dp[0]
