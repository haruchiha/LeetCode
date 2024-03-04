class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        listNumber = []
        for num in range(left, right+1):
            if self.dividingNumber(num):
                listNumber.append(num)
        return listNumber

    def dividingNumber(self, num):
        n = num
        while n > 0:
            if n % 10 == 0 or num % (n % 10) != 0:
                return False
            n = n // 10
        return True
