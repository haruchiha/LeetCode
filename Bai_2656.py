class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort();
        ans = 0;
        num = nums[- 1]
        while (k > 0):
            ans += num
            num += 1
            k -= 1

        return ans
