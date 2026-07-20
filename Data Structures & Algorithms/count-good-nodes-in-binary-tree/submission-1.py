# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        
        def recursion(root:TreeNode, greatestVal:int):
            
            if not root:
                return 0
            
            greatest = greatestVal 

            if(root.val >= greatest):
                self.res += 1
                greatest = root.val

            tmp1 = recursion(root.left, greatest)
            tmp2 = recursion(root.right, greatest)

            return self.res

        return recursion(root, root.val)
        