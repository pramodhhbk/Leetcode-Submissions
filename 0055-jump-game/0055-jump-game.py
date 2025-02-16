class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0]=True
        i=0
        while(dp[i]==True and i<len(nums)-1):
            x = i+nums[i]+1
            dp[i:x] = [True for _ in range(i,x)]
            if(dp[-1]==True):
                return True
            i+=1
        

        return dp[-1]
        