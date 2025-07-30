# Last updated: 7/29/2025, 11:16:23 PM
class Solution(object):
    def maxProfit(self, prices):
        min_price=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            elif prices[i]>min_price:
                profit=max(profit,prices[i]-min_price)
        return profit

               