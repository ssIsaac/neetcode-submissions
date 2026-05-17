class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(0, len(numbers)):
            if((target - numbers[i]) in numbers):
                print(numbers[i])
                return([i+1, numbers.index(target - numbers[i])+1])

            
                