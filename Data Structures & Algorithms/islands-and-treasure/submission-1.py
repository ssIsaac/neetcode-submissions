class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        row, col = len(grid), len(grid[0])

        def addRoom(r,c):
            if (
                r >= 0 and r < row and
                c >= 0 and c < col and 
                (r,c) not in visited and 
                grid[r][c] != -1
            ):
                q.append([r,c])
                visited.add((r,c))
        
        for r in range(row):
            for c in range(col):
                if (grid[r][c] == 0):
                    q.append([r,c])
                    visited.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist += 1




        