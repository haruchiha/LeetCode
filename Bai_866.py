class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        while (True):
            if self.isPrime(n) and self.isPalindrome(n):
                return n
            n += 1
            if (10000000 < n and n < 100030000):  # between 10,000,000 and 100,000,000, there are no prime palindromes
                n = 100030000

    def isPrime(self, n):
        if (n <= 1):
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                return False
        return True

    def isPalindrome(self, n):
        number = n
        tmp = 0
        while (n > 0):
            mod = n % 10
            tmp = tmp * 10 + mod
            n = n // 10
        return (tmp == number)
