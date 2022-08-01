class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        l = 0
        product = 1
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k and l <= r:
                product = product // nums[l]
                l += 1
            count += r - l + 1
        return count
