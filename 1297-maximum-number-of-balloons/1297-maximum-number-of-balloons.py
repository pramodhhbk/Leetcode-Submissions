class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bal = {'b':0,'a':0,'l':0,'o':0,'n':0}
        for i in range(0,len(text)):
            if(text[i] in bal.keys()):
                bal[text[i]]+=1

        
        for i in bal.keys():
            if(bal[i]<=0):
                return 0

        return min(bal['b'],bal['a'],bal['l']//2,bal['o']//2,bal['n'])