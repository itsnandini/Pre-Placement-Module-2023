class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        i, j = 0, 0
    
        res = []
    
        while i < len(firstList) and j < len(secondList):
            low = max(firstList[i][0], secondList[j][0])
            high = min(firstList[i][1], secondList[j][1])
        
            if low <= high:
                res.append([low, high])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
            
        return res
