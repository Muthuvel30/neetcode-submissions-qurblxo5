class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l={}
        for i in nums:
            l[i] = l.get(i,0)+1
        return sorted(l,key=lambda x: l[x],reverse=True)[:k]
        