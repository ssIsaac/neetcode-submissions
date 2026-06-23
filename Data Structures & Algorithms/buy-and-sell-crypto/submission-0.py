class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l,r = 0,1
        while(r < len(prices)):
            diff = prices[r] - prices[l]
            if(diff < 0):
                l = r
                r += 1
            else:
                r += 1
            profit = max(profit, diff)

            
        return profit
