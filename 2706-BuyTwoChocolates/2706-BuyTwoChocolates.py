# Last updated: 7/16/2025, 9:51:23 PM
class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        sum=prices[0]+prices[1]
        if sum<=money:
            return money-sum
        else:
            return money
