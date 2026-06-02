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
                if(height[l] > maxL):
                    maxL = height[l]
                l += 1
            else:
                res += max(0, min(maxL,maxR) - height[r])
                if (height[r] > maxR):
                    maxR = height[r]
                r -= 1

            

            
        return res