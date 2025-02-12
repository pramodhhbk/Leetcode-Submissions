class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        if(len(nums)>=2):
            dp[1] = nums[1]
            for i in range(2,len(nums)):
                dp[i] = nums[i] + max(dp[:i-1])
        
        return max(dp)
    
            
        