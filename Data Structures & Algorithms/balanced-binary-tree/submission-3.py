# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = 0

        def recurr(root:Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            

            nodeL = recurr(root.left)
            nodeR = recurr(root.right)
            if nodeL is False or nodeR is False:
                return False
            self.res = abs(nodeL - nodeR)

            if(self.res > 1):
                return False
            
            return 1 + max(nodeL, nodeR)
        
        tmp = recurr(root)
        if tmp is False:
            return False
        
        return True