class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = set()
        def fn(start, l, tmp):
            if len(tmp) == l:
                ret.add(tuple(tmp))
                return
            
            for i in range(start, len(nums)):
                if i>start and nums[i] == nums[i-1]: continue
                fn(i+1, l, tmp+[nums[i]])
                
        
        for length in range(len(nums)+1):
            fn(0,length,[])
            
        return ret
