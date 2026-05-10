class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    ## Brute force method:
    ## Traverse through the list
    ## Create a dictionary to store the count for each element
    ## Look at the value of k
    ## Return the top k 


        result_temp = defaultdict(int)
        nums.sort()
        
        for i in nums:
            result_temp[i] += 1
        
        # value = list(result)
        # print(value)
        # value.sort(reverse=True)
        # return value[:k]

        result = defaultdict(list)
        for i in (result_temp):
            result[result_temp[i]].append(i)
        print(result)

        arr = []
        result_key = list(result)
        result_key.sort(reverse=True)
        for i in result_key:
            arr += result[i]
        print(arr)
        return arr[:k]
         

        
    
