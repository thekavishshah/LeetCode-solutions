# Last updated: 7/14/2025, 3:28:58 PM
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        a = sorted(d, key=lambda x: d[x], reverse=True)
        return a[:k]
        