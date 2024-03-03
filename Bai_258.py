class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            sum = 0
            while num != 0:
                sum = sum + num % 10
                num = num / 10
            num = sum

        return num
