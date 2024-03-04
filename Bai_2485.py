class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = sum(range(n + 1))
        x_sum = 0

        for i in range(n, -1, -1):
            x_sum += i
            if x_sum == total:
                return i

            total -= i

        return -1
