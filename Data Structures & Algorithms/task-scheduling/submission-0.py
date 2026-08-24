class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) #["X":2, "Y":2]
        queue = deque() #[]
        cycle = 0

        max_heap = [-value for value in count.values()]
        heapq.heapify(max_heap) 

        while(max_heap or queue):
            cycle += 1

            if max_heap:
                temp = 1+heapq.heappop(max_heap) 
                if temp:
                    queue.append([temp,cycle+n]) 
            if(queue and queue[0][1] == cycle):
                temp = queue.popleft()
                heapq.heappush(max_heap, temp[0])
            
             

        return cycle
