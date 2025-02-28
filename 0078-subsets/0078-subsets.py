class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def func(i,l,ans,nums):
            if(i==len(nums)):
                ans.append(l.copy())
                return 
            l.append(nums[i])
            func(i+1,l,ans,nums)
            l.pop()
            func(i+1,l,ans,nums)
            
            return ans

        l = []
        ans = []
        answer = func(0,l,ans,nums)
        return answer

        
