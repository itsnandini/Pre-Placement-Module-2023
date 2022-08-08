class Solution(object):
    def canJump(self, nums):
        max_reach = nums[0]
        end_index = len(nums)-1
        if max_reach >= end_index:
            return True
        for i in range(1, len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i+nums[i])
            if max_reach >= end_index:
                return True            
        return False 
class Solution(object):
    def canJump(self, nums):
        max_reach, i, N = 0, 0, len(nums)
        while i < N and max_reach >= i:
            max_reach = max(max_reach, i+nums[i])
            if max_reach >= N-1:
                return True
            i += 1
        return False
    
