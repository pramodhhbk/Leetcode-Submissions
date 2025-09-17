from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for i in strs:
            count = [0 for _ in range(26)]

            for c in i:
                count[ord(c)-ord('a')]+=1
            
            key = tuple(count)
            ans[key].append(i)
        
        return list(ans.values())
        