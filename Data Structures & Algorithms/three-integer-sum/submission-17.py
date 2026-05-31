class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for n in range(len(nums)):
            if(nums[n] > 0):
                return res
            elif(n > 0 and nums[n] == nums[n-1]):
                continue    
            else:
                l,r = n+1, len(nums)-1
                while(l<r):
                    if(-nums[l] - nums[r] == nums[n]):
                        if(l != n+1 and r != len(nums)-1 and nums[l] == nums[l-1] and nums[r] == nums[r+1]):
                            r -=1 
                            l += 1
                        else:
                            res.append([nums[n], nums[l], nums[r]])
                            r -=1 
                            l += 1
                    elif(-nums[l] - nums[r] < nums[n]):
                        r -= 1 
                    else: 
                        l += 1

        return res