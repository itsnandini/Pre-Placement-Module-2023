class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt, total = 0, 0
        cache = {0:1}
        for v in nums:
            total += v
            if cache.get(total-k):
                cnt += cache[total-k]              
            if cache.get(total):
                cache[total] += 1
            else:
                cache[total] = 1
        return cnt
