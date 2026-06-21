class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l,r = nums[0], nums[-1]
        l,r = 0, len(nums)-1
        
        
        while(l <= r):
            mp = (l + r)//2
            if(nums[mp] == target):
                return mp

            if(nums[l] <= nums[mp]): ##left sorted array
                if(target < nums[l] or target > nums[mp]):
                    l = mp + 1
                else:
                    r = mp - 1

            else:
                if(target > nums[r] or target < nums[mp]):
                    r = mp - 1
                else:
                    l = mp + 1

        return -1
