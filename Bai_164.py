class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if (len(nums) < 2):
            return 0
        result = nums[1] - nums[0]
        for i in range(len(nums) - 1, 0, -1):
            minus = nums[i] - nums[i - 1]
            if minus > result:
                result = minus

        return result

