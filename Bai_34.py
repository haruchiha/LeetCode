# Find First and Last Position of Element in Array
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []  # create a new array
        if target not in nums:
            return [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                a.append(i)

        if (len(a) == 1):
            a.append(a[0])
        elif (len(a) > 2):
            return [a[0], a[-1]]
        return a
