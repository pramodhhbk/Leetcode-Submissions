class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(0,len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)
        while(len(stones)>1):
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if(y!=x):
                heapq.heappush(stones,(y-x))
        
        if(len(stones)>0):
            return -stones[0]
        return 0


        