class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = defaultdict(int)
        arr = [[]*i for i in range(len(nums)+1)]
    

        for i in nums:
            result[i] += 1

        for (key,value) in result.items():
            arr[value].append(key)

        final_result = []
        for i in range(len(arr)-1, 0, -1):
            for j in arr[i]:
                final_result.append(j)
                if (len(final_result)==k):
                    return final_result
        

        
    
