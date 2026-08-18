class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dict_dist = defaultdict(list)
        dist = []
        while points:
            temp2 = points.pop()
            x,y = temp2[0], temp2[1]
            temp = math.sqrt(x*x + y*y)
            dict_dist[temp].append([x,y])
            dist.append(temp)
        heapq.heapify(dist)
        print(dist)

# [
#   2.0, 
#   2.8284271247461903
# ]

# {
#     2.8284271247461903: [[2, 2]], 
#     2.0: [[0, 2]]
# }    
        

        res = []
        count = 0
        while count != k:
            shortest = heapq.heappop(dist)
            if shortest not in dict_dist:
                continue
            coordinates = dict_dist[shortest] ## [[2, 2]]
            for i in coordinates:
                res.append(i)

            count += len(coordinates)
            del dict_dist[shortest]

        return res[:k]


