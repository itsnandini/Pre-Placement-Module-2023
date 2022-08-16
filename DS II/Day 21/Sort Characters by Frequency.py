class Solution:
    def frequencySort(self, s: str) -> str:
        dic=collections.defaultdict(int)
        for st in s:dic[st]+=1
        return ''.join(sorted(s,key=lambda x: (dic[x],ord(x)),reverse=True))
