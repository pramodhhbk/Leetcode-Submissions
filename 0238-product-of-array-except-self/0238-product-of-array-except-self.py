class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_product = [1 for i in range(len(nums))]
        r_product = [1 for i in range(len(nums))]
        final = []
        for i in range(1,len(nums)):
            l_product[i] = nums[i-1] * l_product[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            r_product[i] = nums[i+1] * r_product[i+1]

        for i in range(len(nums)):
            final.append(l_product[i]*r_product[i])
        return final

