# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isbalanced(p,q):
            if not p and not q:
                return True
            
            if (p and not q ) or (not p and q):
                return False
            
            if(p.val!=q.val):
                return False
            
            return isbalanced(p.left,q.left) and isbalanced(p.right,q.right)
        
        return isbalanced(p,q)

            
                


        