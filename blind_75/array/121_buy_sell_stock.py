class Solution:
    #O(n^2) two nested for loops
    def maxProfit1(self, prices: List[int]) -> int:
        max_profit = 0
        for i, day1 in enumerate(prices):
            for j, day2 in enumerate(prices):
                if j > i and day2-day1 > max_profit:
                    max_profit = day2 - day1
                    
        return max_profit
    
    
    #O(n) only one for loop
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        
        for i in prices:
            if i < min_price:
                min_price = i
            max_profit = max(max_profit, i - min_price)
            
        return max_profit