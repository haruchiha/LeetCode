class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        arrNum = []
        for num in nums:
            arrNum.append(int(num))
        arrNum.sort()
        return str(arrNum[len(nums) - k])
