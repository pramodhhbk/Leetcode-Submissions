class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for i in range(len(s)):
            if(s[i]=='(' or s[i]=='[' or s[i]=='{'):
                stack.insert(0,s[i])
            elif(len(stack)>0):
                if(s[i]==')'):
                    if(stack.pop(0)!='('):
                        return False
                elif(s[i]==']'):
                    if(stack.pop(0)!='['):
                        return False
                else:
                    if(stack.pop(0)!='{'):
                        return False
            else:
                return False
        if(len(stack)>0):
            return False
        return True        