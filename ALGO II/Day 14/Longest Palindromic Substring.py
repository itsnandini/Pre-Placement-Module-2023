class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        
        dist = lambda x : x[1]-x[0]
        pos = (0, 0)
        
        for i in range(len(s)) :
            
            odd = self.helper(i, i, s)
            even = self.helper(i, i+1, s)
            
            pos = max(odd, even, pos, key=dist)
            
        return s[pos[0]:pos[1]]
            
    def helper(self, l, r, s):
        
        while l>=0 and r<len(s) and s[l] == s[r] :
            l -= 1
            r += 1
        
        return (l+1, r)
