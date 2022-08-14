class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = amount + 1
        coins.sort(reverse=True)
        dp = [MAX]*(MAX)
        dp[0] = 0
        for i in xrange(1, MAX):
            dp[i] = min([dp[i-c] if i>=c else (MAX) for c in coins]) 
            dp[i] = dp[i] + 1 if dp[i] != MAX else dp[i]
        return -1 if (dp[-1] == MAX) else dp[-1]
