class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.helper(0, candidates, target, [], 0, res)
        return res
        
    def helper(self, i, candidates, target, cur, temp, res):
        for j in range(i, len(candidates)):
            if temp + candidates[j] == target:
                res.append(cur + [candidates[j]])
                return 
            elif temp + candidates[j] < target:
                self.helper(j, candidates, target, cur + [candidates[j]], temp + candidates[j], res)
            else:
                return
