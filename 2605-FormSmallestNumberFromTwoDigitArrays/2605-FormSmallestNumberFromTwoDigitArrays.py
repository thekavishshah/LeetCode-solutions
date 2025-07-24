# Last updated: 7/24/2025, 3:22:37 PM
class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1.sort()
        nums2.sort()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                return nums1[i]
        a=min(nums1)
        b=min(nums2)
        return min(a * 10 + b, b * 10 + a)
        return c
        
        

        