class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## Initialise a variable to keep track of the longest variable 
        ## Loop through the set 
        ## longest = num + longest

        [2,20,4,10,3,4,5]
        longest_global = 0

        nums = set(nums)
        for n in nums:
            if(n-1 not in nums):
                longest_local = 0
                while(n in nums):
                    longest_local += 1
                    n+=1
                longest_global= max(longest_local, longest_global)

        return longest_global 
            
       

