class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        mi = prices[0]
        profit = 0
        
        for x in range(1,len(prices)):
            
            if prices[x] > mi and prices[x] - mi > profit:
                profit = prices[x] - mi
                
            else:
                mi = min(mi,prices[x])
                
        return profit
