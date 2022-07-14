class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        d = []
        d.append(nums[0])
        current_largest_sum = d[0]
        for i in range(1, len(nums)):
            d.append(max(d[i-1] + nums[i], nums[i]))
            if d[i] > current_largest_sum:
                current_largest_sum = d[i]
        return current_largest_sum
