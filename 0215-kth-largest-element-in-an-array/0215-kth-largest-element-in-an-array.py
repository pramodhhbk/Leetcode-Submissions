class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(0,len(nums)):
            nums[i] = -nums[i]
        
        heapq.heapify(nums)
        while(k>1):
            print(k)
            heapq.heappop(nums)
            k-=1
        
        return -heapq.heappop(nums)

            
        