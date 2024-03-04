class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        digit = 0
        for num in nums:
            sum += num

        for num in nums:
            while (num > 0):
                digit += num % 10
                num = num // 10

        return sum - digit