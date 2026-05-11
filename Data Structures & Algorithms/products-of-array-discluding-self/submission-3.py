class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, res = [0]*len(nums), [0]*len(nums)

        temp = 1
        for i in range(len(nums)):
            temp *= nums[i]
            prefix[i] = temp
        temp = 1
        
        postfix = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            temp *= nums[i]
            postfix[i] = temp
        print(postfix)
        for i in range(len(nums)):
            if (i == 0):
                res[i] = postfix[i+1]
            elif (i == (len(nums) -1)):
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1]*postfix[i+1]
        return res


            

