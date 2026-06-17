class Solution:
    def search(self, nums: List[int], target: int) -> int:
        dup = nums.copy()
        while(len(nums) > 0):
            mid = (len(nums)-1)//2
            print(mid)
            if nums[mid] == target:
                return dup.index(target) 
            elif target > nums[mid]:
                nums = nums[mid+1:]
            else:
                nums = nums[:mid]
        return -1


        