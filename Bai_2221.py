class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in range(len(nums), 0, -1):
            for i in range(n - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10

        return nums[0]
