class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            swap = nums[i + 1]
            nums[i + 1] = nums[i]
            nums[i] = swap

        return nums
