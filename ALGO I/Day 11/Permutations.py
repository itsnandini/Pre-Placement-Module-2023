class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)
        def perm(path: List[int]) -> None:
            if len(path) == len(nums):
                ans.append(path)
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                perm(path + [nums[i]])
                used[i] = False
        perm([])
        return ans
