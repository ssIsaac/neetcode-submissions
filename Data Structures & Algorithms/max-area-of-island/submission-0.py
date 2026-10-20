class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def bfs(r,c):
            area = 0
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[0,1],[1,0],[0,-1],[-1,0]]
                for dr,dc in directions:
                    r,c = dr + row, dc + col
                    if (
                        r in range(rows) and c in range(cols) and 
                        (r,c) not in visited and grid[r][c] == 1
                    ):
                        visited.add((r,c))
                        q.append((r,c))
                area += 1
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    temp = bfs(r,c)
                    if temp > maxArea:
                        maxArea = temp
        return maxArea
            


