class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        diff = A[1] - A[0]
        element_count = 2
        result_count = 1
        total = 0
        for i in range(2,len(A)):
            if diff == A[i] - A[i-1]:
                element_count += 1
                if element_count >= 3:
                    total += result_count
                    result_count += 1
            else:
                diff = A[i] - A[i-1]
                element_count = 2
                result_count = 1
        return total
