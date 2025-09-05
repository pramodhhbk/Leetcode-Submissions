class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix,count=0,0
        dic = {0:1}
        for i in range(0,len(nums)):
            prefix+=nums[i]
            remove = prefix -k
            if(remove in dic.keys()):
                count+=dic[remove]
            dic[prefix] = dic.get(prefix,0)+1

        return count