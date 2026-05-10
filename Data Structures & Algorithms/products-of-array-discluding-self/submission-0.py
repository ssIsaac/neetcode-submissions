class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Use a pointer 
        # Product of nums[0:pointer] and nums[pointer+1:]

        res = []
        i = 0
        while (i < len(nums)):
            j = 0
            temp = 1
            while (j < len(nums)):
                if (i != j):
                    temp *= nums[j]                
                j += 1
            res.append(temp)
            i+=1

        return res