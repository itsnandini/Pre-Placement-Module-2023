class Solution:
    def hammingWeight(self, n):
        count = 0
        while n != 0:
            print(n)
            n = n & (n-1)
            count +=1
      
        return count
