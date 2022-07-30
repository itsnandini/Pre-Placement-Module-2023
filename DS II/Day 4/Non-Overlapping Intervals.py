class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        n=len(intervals)
        i=0
        j=1
        count=0
        while j<n:
            if intervals[i][1]<=intervals[j][0]: #Non overlapping
                i=j
                j+=1
            elif intervals[i][1]<=intervals[j][1]: #partial overlapping
                j+=1
                count+=1
            elif intervals[i][1]>=intervals[j][1]: #full overalapping
                i=j
                count+=1
                j+=1
        return count
