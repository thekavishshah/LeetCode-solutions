# Last updated: 6/12/2025, 3:37:03 PM
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        for i in stones:
            if i in jewels:
                count+=1
        return count

        