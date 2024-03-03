class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        factorial = str(factorial)
        count = 0
        for i in range(len(factorial) - 1, 0, -1):
            if factorial[i] == "0":
                count += 1
            else:
                break
        return count
