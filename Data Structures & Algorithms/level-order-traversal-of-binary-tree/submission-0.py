# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return []
        
        queue = deque([root])

        while queue:
            tmp = []
            value = []
            while queue:
                node = queue.popleft()
                tmp.append(node)
                value.append(node.val)
            res.append(value)

            # self.res.append(node)
            for node in tmp:
                if node.left:
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
        return res
