class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        PAC, ATL = set(), set()

        def dfs(r,c,visited,prevHeight):
            if (
                r < 0 or r == ROW or
                c < 0 or c == COL or
                (r,c) in visited or 
                heights[r][c] < prevHeight
            ):
                return 

            visited.add((r,c))
            dfs(r+1,c,visited, heights[r][c])
            dfs(r-1,c,visited, heights[r][c])
            dfs(r,c+1,visited, heights[r][c])
            dfs(r,c-1,visited, heights[r][c])


        for c in range(COL):
            dfs(0,c, PAC, heights[0][c])
            dfs(ROW-1, c, ATL, heights[ROW-1][c])

        for r in range(ROW):
            dfs(r, 0, PAC, heights[r][0])
            dfs(r, COL-1, ATL, heights[r][COL-1])

        result = []
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in PAC and (r,c) in ATL:
                    result.append([r,c])
        
        return result
        
        