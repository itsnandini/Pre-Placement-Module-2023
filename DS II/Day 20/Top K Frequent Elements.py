class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        heap = [(-v,k) for k,v in cnt.items()]
        heapq.heapify(heap)
        ct = 0
        ans = []
        while(ct<k):
            ct+=1
            root = heapq.heappop(heap)
            ans.append(root[1])
        return ans
