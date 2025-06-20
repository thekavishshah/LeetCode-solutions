# Last updated: 6/20/2025, 1:25:52 AM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        a=[]
        b=True
        c=False
        for i in range(0,len(candies)):
            if candies[i]+extraCandies >=max(candies):
                a.append(b)
            else:
                a.append(c)
        return a
                

        