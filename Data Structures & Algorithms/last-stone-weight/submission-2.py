class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        
        heapq.heapify(stones)
        while len(stones) > 1:
            elem1 = heapq.heappop(stones)
            elem2 = heapq.heappop(stones)
            
            if(elem2 > elem1):
                heapq.heappush(stones, elem1 - elem2)

        stones.append(0)
        return abs(stones[0])