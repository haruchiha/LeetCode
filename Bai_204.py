class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Sieve of Eratosthenes
        isPrime = [True] * (n + 1)  # khoi tao tat ca ca so deu la so nguyen to
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i ** 2, n, i):
                    isPrime[j] = False

        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count

