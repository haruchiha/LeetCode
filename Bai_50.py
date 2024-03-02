# Pow(x,n)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if (n == 0):
            return 1
        if (n < 0):
            return (1 / x) / self.myPow(x, -(n + 1));  # 1/(myPow(x,-n))   x^n = x^(n+1) / x = (1/x) / x-(n+1)
        if (n % 2 != 0):
            return x * self.myPow(x, n - 1)

        return self.myPow(x * x, n // 2)