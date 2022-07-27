class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reversed_n = 0
        for i in range(32):
            reversed_n = reversed_n << 1 | ((n >> i) & 1)
        return reversed_n
