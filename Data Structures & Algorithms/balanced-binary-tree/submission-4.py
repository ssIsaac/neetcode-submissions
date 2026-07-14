# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def recurr(root:Optional[TreeNode]) -> int:
            if not root:
                return [True, 0]
            
            

            nodeL = recurr(root.left)
            nodeR = recurr(root.right)
            tmp = abs(nodeL[1] - nodeR[1])
            balanced = (tmp <= 1 and nodeL[0] and nodeR[0])

            
            
            return [balanced, 1 + max(nodeL[1], nodeR[1])]
        
        tmp = recurr(root)
        
        return recurr(root)[0]