class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # using binary search
        left = 0
        right = len(nums) - 1

        while (left < right):
            mid = left + (right - left) // 2

            # Nếu nums[mid] lớn hơn nums[right] thì phần tử nhỏ nhất nằm ở bên phải
            if nums[mid] > nums[right]:
                left = mid + 1
            # Nếu nums[mid] lớn hơn nums[right] thì phần tử nhỏ nhất nằm ở bên trái
            elif nums[mid] < nums[right]:
                right = mid
            # Nếu nums[mid] bằng nums[right], chúng ta không thể loại bỏ phần bên phải ngay lập tức, giảm bên phải đi 1
            else:
                right -= 1

        return nums[left]



