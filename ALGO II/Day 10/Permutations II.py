class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        result = []
        self.permutation(nums, [],result)
        return result

    def permutation(self, numbers, curr, result):
        if len(numbers) == 0:
            result.append(curr)

        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            self.permutation(numbers[0:i]+numbers[i+1:], curr + [numbers[i]], result)
