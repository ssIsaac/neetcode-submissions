class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        while(l <= r):
            midpoint = (l+r)//2 

            if(l == r):
                return nums[r]
            
            elif(l == r -1):
                if (nums[l] < nums[r]):
                    return nums[l]
                return nums[r]

            elif(nums[midpoint] < nums[r]):
                r = midpoint 
            # elif(nums[midpoint] > nums[l] or nums[midpoint] > nums[r]):
            else:
                l = midpoint
                


            

