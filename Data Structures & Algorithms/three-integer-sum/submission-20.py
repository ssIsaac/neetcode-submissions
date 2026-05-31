class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for n,m in enumerate(nums):
            if(m == nums[n-1] and n != 0):
                continue

            l,r = n+1, len(nums)-1

            while(l < r):
                threeSum = m + nums[l] + nums[r]
                if(threeSum < 0):
                    l += 1
                elif(threeSum > 0):
                    r -= 1
                else:
                    res.append([m, nums[l], nums[r]])
                    l += 1
                    while(nums[l] == nums[l-1] and l < r):
                        l += 1
        return res


        # when u encounter the same number, skip it
        # rule follows two sum
        ## for loop: 
        ## 1. if the number is the same as the previous number and it is not the first element in the list, skip
        ## 2. Otherwise do the two sum

        ## while loop:
            # 1. if the number is the same as the previous number and it is not the first element in the list, skip
            # 2. otherwise increment l or decrement r until sum is 0
                    # 1. append into result 