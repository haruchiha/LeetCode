class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for idx in nums:
            if nums.count(idx) == 1:
                return idx
