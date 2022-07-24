class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = []
        
        self.helper(results, s, "", 0)
        
        return results
    
    def helper(self, results, s, permutation, start):
        if len(permutation) == len(s):    
            results.append(permutation)
            return
        
        if s[start].isalpha():
            self.helper(results, s, permutation + s[start].upper(), start + 1)
            self.helper(results, s, permutation + s[start].lower(), start + 1)            
        else:
            self.helper(results, s, permutation + s[start], start + 1)
