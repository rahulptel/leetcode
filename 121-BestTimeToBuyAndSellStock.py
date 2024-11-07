class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_profit = 0
        
        while j < len(prices):
            diff = prices[j] - prices[i]
            if diff > 0:
                if diff > max_profit:
                    max_profit = diff
            else:
                i = int(j)

            j += 1
            
        return max_profit


        
