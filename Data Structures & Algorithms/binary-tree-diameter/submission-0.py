# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0 
        
        ## find height
        def recurr(root:Optional[TreeNode]) -> int:
            if not root:
                return 0

            heightL = recurr(root.left)
            heightR = recurr(root.right)
            
            self.diameter = max(self.diameter, heightL+heightR)

            return 1 + max(heightL, heightR)

        recurr(root)
        return self.diameter
