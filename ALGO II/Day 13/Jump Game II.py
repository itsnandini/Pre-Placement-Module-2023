class Solution(object):
    def jump(self, nums):
        res = 0
        edge = 0
        maxEdge = 0
        for i in range(len(nums)):
            if i > edge:
                edge = maxEdge
                res += 1
            maxEdge = max(maxEdge,i+nums[i])
        return res
