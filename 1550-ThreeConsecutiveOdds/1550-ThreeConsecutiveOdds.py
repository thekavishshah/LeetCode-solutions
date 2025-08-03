# Last updated: 8/3/2025, 12:27:16 AM
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count=0
        for i in range(0,len(arr)):
            if arr[i]%2==1:
                count+=1

                if count==3:
                    return True
            else:
                count=0
        return False