# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def recurr(root: Optional[TreeNode], left, right):
            if not root:
                return True
            if root.val >= right or root.val <= left:
                return False
            
            
            tmp1 = recurr(root.left,left, root.val)
            tmp2 = recurr(root.right, root.val, right)

            return (tmp1 and tmp2)

        return recurr(root, float("-inf"), float("inf"))