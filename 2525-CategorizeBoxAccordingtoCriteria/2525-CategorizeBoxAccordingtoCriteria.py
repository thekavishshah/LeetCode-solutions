# Last updated: 7/23/2025, 3:13:05 PM
class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        bulky=False
        heavy=False
        a=10**4
        if length>=a or width>=a or height >=a or mass>=a:
            bulky=True
        if length*width*height>=10**9:
            bulky=True
        if mass>=100:
            heavy=True
        if bulky==True and heavy==True:
            return "Both"
        if bulky==False and heavy==False:
            return "Neither"
        if bulky==True and heavy==False:
            return "Bulky"
        if bulky==False and heavy==True:
            return "Heavy"
        
        
        
        