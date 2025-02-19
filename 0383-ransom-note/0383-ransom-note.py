class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = len(ransomNote)
        m = len(magazine)
        ransom = {key:0 for key in ransomNote}
        mag = {key:0 for key in magazine}
        for i in range(0,len(ransomNote)):
            ransom[ransomNote[i]]+=1
        for i in range(0,len(magazine)):
            mag[magazine[i]]+=1
        
        for key in ransom.keys():
            if(key not in mag.keys() or ransom[key]>mag[key]):
                return False
            
        
        return True
        

        
        



        