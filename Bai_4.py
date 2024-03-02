#Median of Two Sorted Arrays
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2  #merge two arrays

        num.sort()
        length = len(num)
        if length % 2 == 0:
            return (num[length//2-1] + num[length//2])/2.0
        return num[length//2]

