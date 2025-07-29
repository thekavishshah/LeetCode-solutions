# Last updated: 7/29/2025, 12:15:07 AM
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(0,len(arr)):
            a=arr[i]*2
            for j in range(0,len(arr)):
                if i!=j and arr[j]==a:
                    return True
        return False
            