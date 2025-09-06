class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {x:0 for x in nums}
        for i in nums:
            dic[i]+=1
        s = ((-v,-k) for k,v in dic.items())
        s = list(s)
        heapq.heapify(s)
        flist = []
        while(k>0):
            x = heapq.heappop(s)
            flist.append(-x[1])
            k-=1

        return flist
        
        