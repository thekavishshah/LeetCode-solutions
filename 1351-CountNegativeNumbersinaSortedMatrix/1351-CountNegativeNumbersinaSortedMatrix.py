# Last updated: 7/29/2025, 12:16:50 AM
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j]<0:
                    count+=1
        return count


        