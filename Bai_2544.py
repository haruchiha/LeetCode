class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        sign = 1

        while n > 0:
            sign *= -1
            sum += sign*(n%10)
            n = n // 10
        return sum*sign

