class Solution:
    def trap(self, height: List[int]) -> int:
        """
        1. increment min(maxL, maxR)

        """
        res = 0
        l, r = 0, len(height)-1
        maxL,maxR = height[l], height[r]
        while(l<=r):
            if(maxL <= maxR):
                res += max(0, min(maxL,maxR) - height[l])
                maxL = max(height[l], maxL)
                l += 1
            else:
                res += max(0, min(maxL,maxR) - height[r])
                maxR = max(height[r], maxR)
                r -= 1

            

            
        return res