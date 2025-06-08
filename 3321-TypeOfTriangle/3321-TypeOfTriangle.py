# Last updated: 6/7/2025, 7:02:40 PM
class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a=nums[0]
        b=nums[1]
        c=nums[2]

        if a+b <=c or a+c<=b or b+c<=a:
            return "none"
        if a==b==c:
            return "equilateral"
            
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"
    

        

        