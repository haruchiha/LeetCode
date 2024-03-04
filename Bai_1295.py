class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            if self.numOfDigits(num) % 2 == 0:
                result += 1

        return result

    def numOfDigits(self, nums):
        count = 0
        while (nums > 0):
            nums = nums // 10
            count += 1
        return count

