# Last updated: 6/7/2025, 11:36:51 PM
class Solution(object):
    def containsDuplicate(self, a):
        b=set()
        for i in a:
            if i in b:
                return True
            else:
                b.add(i)
        return False
            