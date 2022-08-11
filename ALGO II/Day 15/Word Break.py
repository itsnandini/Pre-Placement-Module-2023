class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp, truelist = [False] * len(s), []
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp[i] = True
                truelist.append(i)
                continue
            for j in truelist:
                if s[j+1:i+1] in wordDict:
                    dp[i] = True
                    truelist.append(i)
                    break
        return dp[-1]
