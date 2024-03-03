class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_of_n = (n + 1) * n // 2  # sum of n
        sum_of_nums = 0
        for i in range(0, len(nums)):
            sum_of_nums += nums[i]
        return sum_of_n - sum_of_nums
