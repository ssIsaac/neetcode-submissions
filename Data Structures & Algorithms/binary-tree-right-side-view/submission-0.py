# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])

        while(queue):
            qLen = len(queue)
            check = True
            for i in range(len(queue)):
                node = queue.pop()
                if node: 
                    if check:
                        res.append(node.val)
                        check = False
                    queue.appendleft(node.right)
                    queue.appendleft(node.left)
        
        return res



