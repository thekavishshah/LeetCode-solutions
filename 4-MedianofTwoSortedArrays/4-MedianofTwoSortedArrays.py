# Last updated: 6/12/2025, 4:36:55 PM
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)
        if n%2==0:
            return (nums1[n//2] + nums1[n//2 -1]) /2.0
        else:
            return nums1[(n/2)]
