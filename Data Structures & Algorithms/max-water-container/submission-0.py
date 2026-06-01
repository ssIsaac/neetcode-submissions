class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ## find the two longest heights 
        ## output is the min(height1. height2)*width

        volume = 0
        l,r = 0, len(heights)-1
        while(l<r):
            volume = max(volume, min(heights[l], heights[r])* (r-l))
            if(heights[l] > heights[r]):
                r -= 1
            else:
                l += 1

        return volume
