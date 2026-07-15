# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True
        
        def preOrder(p:Optional[TreeNode], q:Optional[TreeNode]):
            if not p and not q:
                return True
            if (not p or not q) or p.val != q.val:
                return False
            
            
            
            leftNode = preOrder(p.left, q.left)
            rightNode = preOrder(p.right, q.right)

            return (leftNode and rightNode)
       
        return preOrder(p,q)
             
            
        
