class Solution:
    def _subsets(self, nums:List[int], current: List[int], index:int):        
        if index>=len(nums):           
            self.sol.append(current)
            return
        # solution adding the nums[index]
        self._subsets(nums, current+[nums[index]], index+1)
        # solution ignoring nums[index]
        self._subsets(nums, current, index+1)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.sol = []
        self._subsets(nums,[], 0)
        return self.sol
