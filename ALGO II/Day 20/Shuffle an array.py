class Solution(object):

    def __init__(self, nums):
        self.original_array = nums
        """
        :type nums: List[int]
        """
        

    def reset(self):
        return self.original_array
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        

    def shuffle(self):
        arr = self.original_array[:]
        for x in range(len(self.original_array)):
            n = random.randint(0, x)
            arr[x],arr[n] = arr[n], arr[x]
        return arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
