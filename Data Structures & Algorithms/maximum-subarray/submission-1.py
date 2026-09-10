class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, maxSum = 0, nums[0]
        for i in nums:
            sum += i
            maxSum = max(maxSum, sum)
            if sum < 0:
                sum = 0
        return maxSum
            
