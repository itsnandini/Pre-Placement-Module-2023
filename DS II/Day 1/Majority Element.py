class Solution(object):
    def majorityElement(self, nums):
        candi, count = 0, 0
        for num in nums:
            if count == 0:
                candi = num
                count += 1
            elif num == candi:
                count += 1
            else:
                count -= 1
        return candi
