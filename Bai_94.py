# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is not None:
            # Duyệt cây con trái
            result += self.inorderTraversal(root.left)

            # Lưu giá trị nút hiện tại
            result.append(root.val)

            # Duyệt cây con phải
            result += self.inorderTraversal(root.right)
        return result

