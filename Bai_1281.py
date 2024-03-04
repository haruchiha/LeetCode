class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum_of_n = 0
        product_of_n = 1
        while (n > 0):
            mod = n % 10
            sum_of_n += mod
            product_of_n *= mod
            n = n // 10
        return product_of_n - sum_of_n
