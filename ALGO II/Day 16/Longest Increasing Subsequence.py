class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        n=len(nums)
        l=[1]*n
        for i in range (1,n): 
            for j in range(i): 
                if nums[i]>nums[j] and l[i]<=l[j]: 
                    l[i]=l[j]+1
        return max(l)
