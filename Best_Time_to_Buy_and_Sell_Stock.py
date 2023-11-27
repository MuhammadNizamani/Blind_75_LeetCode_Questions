
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = prices[0]
        max_profit = 0
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_profit:
                max_profit = i - min_price
        return max_profit

      
  
        


sol = Solution()
max_profit = sol.maxProfit(prices=[7,1,5,3,6,4])
print(max_profit)