# Last updated: 7/25/2025, 4:41:49 PM
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        a=nums1[0:m]
        a.extend(nums2)
        a.sort()
        nums1[:]=a

