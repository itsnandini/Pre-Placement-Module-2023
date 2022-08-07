class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result
        d = {'2': 'abc',
             '3': 'def',
             '4': 'ghi',
             '5': 'jkl',
             '6': 'mno',
             '7': 'pqrs',
             '8': 'tuv',
             '9': 'wxyz'
            }
        s = list(digits)
        def perm(pre,s):
            if not s:
                result.append(''.join(pre))
                return
            for char in d[s[0]]:
                perm(pre+[char],s[1:])
        perm([],s)
        return result
