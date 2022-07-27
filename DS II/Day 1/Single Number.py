class Solution(object):
    def singleNumber(self, nums):
        map = {}
        if ( nums == [] ):
            return -1
        for d in nums:
            if ( d in map):
                del map[d]
            else:
                map[d] = 1
        return list(map.keys())[0]
