class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        i = 1
        result = 1
        while result * result <= x:
            i += 1
            result = i

        return result - 1
