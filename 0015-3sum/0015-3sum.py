class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        final_lst = []
        s =set()
        
        for i in range(0,len(nums)-2):
            if(nums[i] not in s):
                s.add(nums[i])
                cur_sum = 0 - nums[i]
                l =i+1
                r = len(nums)-1
                
                while(l<r):
                    
                    if(nums[l] + nums[r]== cur_sum):
                        final_lst.append([nums[i],nums[l],nums[r]])
                        
                        l+=1
                        r-=1
                    elif(nums[l]+nums[r]<cur_sum):
                        l+=1
                    else:
                        r-=1

        print(final_lst) 
        skt = set(tuple(i) for i in final_lst)
        kk = [list(i) for i in skt]
        print(kk)
        return kk

        