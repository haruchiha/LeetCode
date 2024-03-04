class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = 0
        for num in nums:
            if num == 0:
                count = 0
            else:
                count += 1
                result = max(result, count)
        return result
