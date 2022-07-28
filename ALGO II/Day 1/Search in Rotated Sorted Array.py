class Solution:
    def search(self, nums, target):    
        def search(nums, l, r):
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if l == r:
                return -1
            if nums[l] < nums[m]:
                if target >= nums[l] and target < nums[m]:
                    return search(nums, l, m - 1)
                else:
                    return search(nums, m + 1, r)
            elif r - m == 1:
                if nums[r] == target:
                    return r
                else:
                    return search(nums, l, m)
            elif nums[m + 1] < nums[r]:
                if target >= nums[m + 1] and target <= nums[r]:
                    return search(nums, m + 1, r)
                else:
                    return search(nums, l, m - 1)
            return -1

        return -1 if not nums else search(nums, 0, len(nums) - 1)
