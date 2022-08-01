class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        c = collections.Counter(p)
        cur = collections.Counter(s[:len(p)])
        for i in range(len(s)-len(p)+1):
            if cur==c:
                res.append(i)
            if i == len(s)-len(p):
                break
            cur[s[i]]-=1
            if cur[s[i]]==0:
                del cur[s[i]]
            cur[s[i+len(p)]]+=1
        return res
