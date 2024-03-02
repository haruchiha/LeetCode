# First Missing Positive
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        n = len(nums)

        for i in range(1, n + 2):
            if i not in num_set:
                return i

        # a set in python is an unordered collection of unique elements
