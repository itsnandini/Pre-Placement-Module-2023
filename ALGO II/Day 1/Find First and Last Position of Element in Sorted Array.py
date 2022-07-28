class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.findStart(nums, target)
        end = self.findEnd(nums, target)
        return [start, end]
    
    def findStart(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        start = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                start = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return start
    
    def findEnd(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        end = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                end = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return end
