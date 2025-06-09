# Last updated: 6/8/2025, 7:13:45 PM
class Solution(object):
    def intersection(self, nums1, nums2):
        a=[]
        for i in range(0, len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in a:
                a.append(nums1[i])
        return a