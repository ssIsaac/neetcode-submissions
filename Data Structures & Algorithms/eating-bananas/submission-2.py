class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        # rates = list(range(1, piles[-1]+1))
        l, r = 1, piles[-1]
        rate = 0

        while(l <= r):
            mid_value = (l+r)//2
            time_taken = 0
            for i in piles:
                time_taken += (i + mid_value - 1)//mid_value ##round up
            # print(time_taken)
            if time_taken > h:
                l = mid_value + 1
            else:
                rate = mid_value
                r = mid_value - 1
            # print(rate)
        
        return int(rate)



        
        