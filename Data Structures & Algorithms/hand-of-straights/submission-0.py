class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand)%groupSize):
            return False

        handDict = defaultdict(int)
        for i in hand:
            handDict[i] += 1
        # print(handDict)
        minH = list(handDict.keys())
        heapq.heapify(minH)

        while minH:
            smallest = minH[0]
            for i in range(groupSize):
                if smallest not in handDict:
                    # print("1")
                    return False
                handDict[smallest] -= 1
                if handDict[smallest] == 0:
                    popped = heapq.heappop(minH)
                    
                    if popped != smallest:
                        return False


                smallest += 1
        
        return True

