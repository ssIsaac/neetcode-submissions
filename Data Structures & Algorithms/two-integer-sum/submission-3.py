class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## loop through the list 
        ## nums - var[i] = answer
        ## if answer is in list, find index(answer)
        ## Add i and index(answer) into an array
        ## return answer

        arr = []
        for i in range (len(nums)): 
            j = target - nums[i]
            if j in nums and (i != nums.index(j)):
                arr = [i, nums.index(j)]
                arr.sort()
                break
        return arr