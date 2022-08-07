def parenthesis(n,i,ans,s,op,cl):
    if cl > op or cl > n or op > n: return
    if op == n and cl == n:
        ans.append(s)
        return
    parenthesis(n,i+1,ans,s+"(",op+1,cl)
    parenthesis(n,i+1,ans,s+")",op,cl+1)  
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        parenthesis(n,0,ans,"",0,0)
        return ans
