class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2: return 1
        if n == 3: return 2
        if n == 4: return 4
        if n % 3 == 0: return 3**(n/3)
        if (n-4)%3 == 0:
            return 3**((n-4)/3)*4
        else:
            return 3**((n-2)/3)*2
