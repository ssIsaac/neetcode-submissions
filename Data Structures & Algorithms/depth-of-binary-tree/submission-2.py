# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return self.recursive(root, 1)
        return 0

    def recursive(self, root: Optional[ThreeNode], count) -> int:
        
        tmp1 = tmp2 = count

        print(root.val)
        if root.left:
            tmp1 = self.recursive(root.left, count+1)
        
        if root.right:
            tmp2 = self.recursive(root.right, count+1)
        
        return max(tmp1,tmp2)
