# Last updated: 7/28/2025, 1:35:51 PM
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        a=""
        for i in range(0,len(address)):
            if address[i]==".":
                a+="[.]"
            else:
                a+=address[i]
        return a