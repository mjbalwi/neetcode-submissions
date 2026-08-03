class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        for r in range(len(prices)):
            
            if prices[r] > prices[l]:
                diff = prices[r] - prices[l]
                maxP = max(diff, maxP)
            elif prices[l] > prices[r]:
                l = r
        
        return maxP


        