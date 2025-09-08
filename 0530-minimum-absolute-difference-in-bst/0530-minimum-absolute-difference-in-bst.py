# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        lst = []
        def inorder(root):
            if not root:
                return 
            
            inorder(root.left)
            lst.append(root.val)
            inorder(root.right)
        
        if not root:
            return 0
        inorder(root)
        print(lst)

        for i in range(0,len(lst)-1):
            lst[i] = lst[i+1] - lst[i]
        
        return min(lst)
            


                
            
            
        