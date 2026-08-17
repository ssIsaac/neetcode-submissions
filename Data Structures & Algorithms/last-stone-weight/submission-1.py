class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        self.minHeap = stones
        heapq.heapify(self.minHeap)
        while(len(self.minHeap) > 1):
            elem1 = heapq.heappop(self.minHeap)
            elem2 = heapq.heappop(self.minHeap)
            resultant = elem1 - elem2 
            if(resultant == 0):
                continue
            else:
                heapq.heappush(self.minHeap, resultant)
        return -(self.minHeap[0]) if self.minHeap else 0