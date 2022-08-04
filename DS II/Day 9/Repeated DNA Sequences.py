class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mp = {}
        res = set()
        for i in range(len(s)-9):
            k = s[i:i+10]
            mp[k] = mp.get(k,0) + 1
            if mp[k] > 1:
                res.add(k)
        return list(res)
