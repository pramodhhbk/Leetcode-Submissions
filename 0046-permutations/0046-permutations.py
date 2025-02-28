class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack():
            if(len(sol)==len(nums)):
                ans.append(sol.copy())
                return
            
            for x in nums:
                if(x not in sol):
                    sol.append(x)
                    backtrack()
                    sol.pop()

        ans ,sol = [],[]    
        backtrack()
        return ans

        