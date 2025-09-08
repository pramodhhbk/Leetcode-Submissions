# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has(root,cur_sum):
            if not root:
                return False
            
            cur_sum+=root.val
            
            if not root.left and not root.right:
                return cur_sum == targetSum
            
            

            return has(root.left,cur_sum) or has(root.right,cur_sum)
        
        return has(root,0)
        