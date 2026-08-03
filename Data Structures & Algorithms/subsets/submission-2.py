class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
            return
        dfs(0)
        return res

"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        dfs(0)
        return res


dfs(0):
    if i >= len(nums):
        res.append(subset.copy())
        return
    
    subset.append(1)
    dfs(i+1)

dfs(1):
    if i >= len(nums):
        res.append(subset.copy())
        return
    
    subset.append(2)
    dfs(2)

dfs(2):
    if i >= len(nums):
        res.append(subset.copy())
        return
    
    subset.append(3)
    dfs(3)



dfs(3):
    if i >= len(nums):
        res.append(subset.copy())
        return

res = [[1,2,3]]



dfs(2):
    if i >= len(nums):
        res.append(subset.copy())
        return
    
    subset.append(3)
    dfs(3)

    subset.pop()
    ## subset = [1,2]
    dfs(3)

dfs(3):
    if i >= len(nums):
        res.append(subset.copy())
        return

res = [[1,2,3], [1,2]]

dfs(1):
    if i >= len(nums):
        res.append(subset.copy())
        return
    
    subset.append(2) ##subset: [1,2]
    dfs(2)

    subset.pop(2) ##subset: [1]
    dfs(2)

def dfs(2):
    if i >= len(nums):
        res.append(subset.copy())
        return
    
    subset.append(3)##subset: [1,3]
    dfs(3)

def dfs(3):
    if i >= len(nums):
        res.append(subset.copy())
        return

res = [[1,2,3],[1,2],[1,3]]

def dfs(2):
    if i >= len(nums):
        res.append(subset.copy())
        return
    
    subset.append(3)##subset: [1,3]
    dfs(3)

    subset.pop(3) ##subset: [1]
    dfs(3)

def dfs(3):
    if i >= len(nums):
        res.append(subset.copy()) 
        return

res = [[1,2,3],[1,2],[1,3],[1]]

# -----------------------------------------------
dfs(0):
    if i >= len(nums):
        res.append(subset.copy())
        return
    
    subset.append(1)
    dfs(2)

    subset.pop() ##subset = []
    dfs(1)

dfs(1):
    if i >= len(nums):
        res.append(subset.copy())
        return
    
    subset.append(1) ##subset = [2]
    dfs(2)

dfs(2):
    if i >= len(nums):
        res.append(subset.copy())
        return
    
    subset.append(3) ##subset = [2,3]
    dfs(3)

dfs(3):
    if i >= len(nums):
        res.append(subset.copy())
        return


res = [[1,2,3],[1,2],[1,3],[1], [2,3]]


dfs(2):
    if i >= len(nums):
        res.append(subset.copy())
        return
    
    subset.append(3) ##subset = [2,3]
    dfs(3)

    subset.pop() ##subset = [2]
    dfs(3)

dfs(3):
    if i >= len(nums):
        res.append(subset.copy())
        return 

res = [[1,2,3],[1,2],[1,3],[1], [2,3], [2]]

dfs(1):
    if i >= len(nums):
        res.append(subset.copy())
        return
    
    subset.append(1) 
    dfs(2)

    subset.pop() ##subset = []
    dfs(2)

dfs(2):
    if i >= len(nums):
        res.append(subset.copy())
        return
    
    subset.append(2) ##subset = [3]
    dfs(3)

dfs(3):
    if i >= len(nums):
        res.append(subset.copy())
        return 

res = [[1,2,3],[1,2],[1,3],[1], [2,3], [2], [3]]

dfs(2):
    if i >= len(nums):
        res.append(subset.copy())
        return
    
    subset.append(2) ##subset = [3]
    dfs(3)

    subset.pop() ##subset = []
    dfs(3)

dfs(3):
    if i >= len(nums):
        res.append(subset.copy())
        return 

res = [[1,2,3],[1,2],[1,3],[1], [2,3], [2], [3],[]]

"""
        