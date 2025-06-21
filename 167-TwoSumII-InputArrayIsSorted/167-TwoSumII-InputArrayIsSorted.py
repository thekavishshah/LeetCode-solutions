# Last updated: 6/20/2025, 7:21:48 PM
class Solution(object):
    def twoSum(self, numbers, target):
        i=0
        j=len(numbers)-1
        while i<j:
            sum=numbers[i]+numbers[j]
            if sum==target:
                return [i+1,j+1]
            if sum<target:
                i+=1
            else:
                j-=1