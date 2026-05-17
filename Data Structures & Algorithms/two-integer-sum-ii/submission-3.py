class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            for j in range (1, len(numbers)):
                if(target - numbers[j] == numbers[i]):
                    print(numbers[i])
                    print(numbers[j])
                    return [i+1,j+1]
                continue
                